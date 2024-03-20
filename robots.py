import pymongo 
from datetime import datetime
import time
while True:
    basexml = """

    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

    <url>
    <loc>https://www.kentel.dev/</loc>
    <lastmod>2024-02-11T13:04:29+00:00</lastmod>
    <priority>1.00</priority>
    </url>
    <url>
    <loc>https://www.kentel.dev/login</loc>
    <lastmod>2024-02-11T13:04:29+00:00</lastmod>
    <priority>0.80</priority>
    </url>
    <url>
    <loc>https://www.kentel.dev/signup</loc>
    <lastmod>2024-02-11T13:04:29+00:00</lastmod>
    <priority>0.80</priority>
    </url>
    <url>
    <loc>https://www.kentel.dev/about</loc>
    <lastmod>2024-02-11T13:04:29+00:00</lastmod>
    <priority>0.80</priority>
    </url>
    <url>
    <loc>https://www.kentel.dev/faq</loc>
    <lastmod>2024-02-11T13:04:29+00:00</lastmod>
    <priority>0.80</priority>
    </url>
    <url>
    <loc>https://www.kentel.dev/kentel-eula</loc>
    <lastmod>2024-02-11T13:04:29+00:00</lastmod>
    <priority>0.64</priority>
    </url>

    """
    mongo = pymongo.MongoClient()
    db = mongo["KentelPlatform"]
    blog = db["blog"]

    allBlogPosts = blog.find({"category":"blog","visible":True})
    for b in allBlogPosts:
        timestamp = b["time"]
        dt = datetime.fromtimestamp(timestamp)
        ds = dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        ld = f"""
            <url>
    <loc>https://www.kentel.dev/blog/{b['_id']}</loc>
    <lastmod>{ds}</lastmod>
    <priority>0.7</priority>
    </url>
        """
        basexml += ld

    #after creation
    basexml += "</urlset>"
    open("other/sitemap.xml","w").write(basexml)
    time.sleep(80000)