# 🕷️ Crawl4AI Tutorial

## 📌 What is Crawl4AI?
**Crawl4AI** is an open-source web crawling framework designed specifically for extracting web content and formatting it for Large Language Models (LLMs). It converts messy HTML pages into structured, readable Markdown.

## 🚀 Why Crawl4AI?
- **🧠 Built for LLMs**: Produces clean, RAG/fine-tune-ready Markdown.
- **⚡ Lightning Fast**: Up to 6x faster performance.
- **🌍 Flexible Browser Control**: Includes session management, proxies, and custom hooks.
- **🔍 Heuristic Intelligence**: Smart extraction with reduced model cost.
- **📦 Open Source**: Fully open-source and Docker/cloud ready.
- **🌐 Thriving Community**: Actively maintained, trending on GitHub.

## 🧪 Basic Crawl4AI Example - Single Page Crawl

```bash
pip install -U crawl4ai
crawl4ai-setup
```

```python
import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://ai.pydantic.dev/")
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
```

## 🤝 Ethics of Web Scraping
Always respect `robots.txt` rules of a website (e.g., `youtube.com/robots.txt`). Scraping responsibly is essential!

## 🌐 Crawling Multiple Pages via Sitemap

```python
# Fetch sitemap, extract URLs and crawl each
# See full tutorial code for details
```

## ⚡ Fast Parallel Page Crawling

To maximize speed, Crawl4AI allows parallel crawling.

```bash
pip install psutil
```

```python
# Parallel crawling code that checks memory and reuses browser sessions
# See full tutorial code for details
```

## 📁 Output
Crawled content is converted to Markdown, ideal for downstream tasks like summarization, training, or search.

---

**Made with ❤️ using medrhouma**.
