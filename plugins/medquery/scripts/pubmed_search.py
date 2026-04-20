"""Programmatic PubMed search using NCBI E-utilities.

Usage:
    python pubmed_search.py "crispr gene editing" --max 20
    python pubmed_search.py "covid vaccine" --max 10 --json

Optionally set NCBI_API_KEY env var for higher rate limits (10/s vs 3/s).
See: https://www.ncbi.nlm.nih.gov/books/NBK25501/
"""

import argparse
import json
import os
import ssl
import sys
import time
from typing import Any
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import xml.etree.ElementTree as ET

try:
    import certifi
    _SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CTX = None

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "pubmed-search-script"
EMAIL = os.environ.get("NCBI_EMAIL", "")
API_KEY = os.environ.get("NCBI_API_KEY", "")


def _request(path: str, params: dict[str, Any]) -> bytes:
    params = {**params, "tool": TOOL}
    if EMAIL:
        params["email"] = EMAIL
    if API_KEY:
        params["api_key"] = API_KEY
    url = f"{EUTILS}/{path}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": TOOL})
    with urlopen(req, timeout=30, context=_SSL_CTX) as resp:
        return resp.read()


def esearch(query: str, retmax: int = 20) -> tuple[list[str], int]:
    """Return (pmids, total_count) for the query."""
    data = _request("esearch.fcgi", {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json",
    })
    payload = json.loads(data)["esearchresult"]
    return payload.get("idlist", []), int(payload.get("count", 0))


def efetch(pmids: list[str]) -> list[dict[str, Any]]:
    """Fetch full article metadata for the given PMIDs."""
    if not pmids:
        return []
    data = _request("efetch.fcgi", {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    })
    root = ET.fromstring(data)
    results = []
    for article in root.findall(".//PubmedArticle"):
        results.append(_parse_article(article))
    return results


def _parse_article(article: ET.Element) -> dict[str, Any]:
    def text(path: str) -> str:
        el = article.find(path)
        return "".join(el.itertext()).strip() if el is not None else ""

    pmid = text(".//PMID")
    title = text(".//ArticleTitle")
    abstract = " ".join(
        "".join(el.itertext()).strip()
        for el in article.findall(".//Abstract/AbstractText")
    )
    journal = text(".//Journal/Title")
    year = text(".//PubDate/Year") or text(".//PubDate/MedlineDate")[:4]
    doi = ""
    for el in article.findall(".//ArticleId"):
        if el.attrib.get("IdType") == "doi":
            doi = (el.text or "").strip()
            break
    authors = []
    for a in article.findall(".//Author"):
        last = a.findtext("LastName") or ""
        init = a.findtext("Initials") or ""
        collective = a.findtext("CollectiveName") or ""
        name = f"{last} {init}".strip() or collective
        if name:
            authors.append(name)
    return {
        "pmid": pmid,
        "title": title,
        "authors": authors,
        "journal": journal,
        "year": year,
        "doi": doi,
        "abstract": abstract,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }


def search(query: str, max_results: int = 20) -> list[dict[str, Any]]:
    pmids, _ = esearch(query, retmax=max_results)
    # Respect rate limits (3 req/s without key, 10 with)
    time.sleep(0.34 if not API_KEY else 0.11)
    return efetch(pmids)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search PubMed.")
    parser.add_argument("query", help="Search query (PubMed syntax supported)")
    parser.add_argument("--max", type=int, default=10, help="Max results (default 10)")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    results = search(args.query, max_results=args.max)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    for i, r in enumerate(results, 1):
        authors = ", ".join(r["authors"][:3])
        if len(r["authors"]) > 3:
            authors += ", et al."
        print(f"[{i}] {r['title']}")
        print(f"    {authors}")
        print(f"    {r['journal']} ({r['year']}) PMID:{r['pmid']} DOI:{r['doi']}")
        print(f"    {r['url']}")
        if r["abstract"]:
            snippet = r["abstract"][:280] + ("..." if len(r["abstract"]) > 280 else "")
            print(f"    {snippet}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
