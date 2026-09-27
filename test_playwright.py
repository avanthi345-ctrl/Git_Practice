def test_playwright(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()