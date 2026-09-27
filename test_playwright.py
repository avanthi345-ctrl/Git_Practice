def test_playwright(page):
    page.goto("https://example.com")
    assert "Wrong Title" in page.title()