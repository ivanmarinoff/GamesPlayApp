from playwright.sync_api import Page, expect


# def test_home_page_to_be_visible(page: Page) -> None:
#     page.goto("localhost:3000/")
#     expect(page).to_have_url("http://localhost:3000/")
#     expect(page.locator("h1")).to_contain_text("GamesPlay")
#     expect(page.get_by_role("navigation")).to_contain_text("Dashboard")
#     expect(page.get_by_role("navigation")).to_contain_text("Create Game")
#     expect(page.get_by_role("navigation")).to_contain_text("Profile")
#     expect(page.get_by_role("heading", name="ALL new games are")).to_be_visible()
#     expect(page.get_by_role("heading", name="Only in GamesPlay")).to_be_visible()


# def test_dashboard_to_be_visible(page: Page) -> None:
#     page.goto("http://localhost:3000/profile/dashboard/")
#     expect(page).to_have_url("http://localhost:3000/profile/dashboard/")

def test_create_game_to_be_visible(page: Page) -> None:
    page.goto("http://localhost:3000/game/create/")
    expect(page).to_have_url("http://localhost:3000/game/create/")
    expect(page.get_by_role("button", name="Create Game")).to_be_visible()
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("Test Game")

    page.get_by_label("Category:").click()
    page.get_by_label("Category:").select_option("Other")

    page.get_by_label("Rating:").click()
    page.get_by_label("Rating:").fill("5")
    page.get_by_label("Max level:").click()
    page.get_by_label("Max level:").fill("10")
    page.get_by_label("Image url:").click()
    page.get_by_label("Image url:").fill("https://ichef.bbci.co.uk/news/976/cpsprodpb/13729/production/_112375697_1331db7a-17c0-4401-8cac-6a2309ff49b6.jpg")
    page.get_by_label("Summary:").click()
    page.get_by_label("Summary:").fill("Amazon Crucible: 'Can games be as fun to watch as they are to play?'Crucible is a new free-to-play PC game and is a competitive shooting title that's a cross between Overwatch, Gears of War and League of Legends.")
    page.get_by_role("button", name="Create Game").click()
    expect(page).to_have_url("http://localhost:3000/profile/dashboard/")

    
    # page.get_by_role("link", name="Profile").click()
    # expect(page.locator("#game-details")).to_contain_text("Profile Details")
    # expect(page.get_by_role("link", name="Edit")).to_be_visible()
    # expect(page.get_by_role("link", name="Delete")).to_be_visible()
    # page.get_by_role("link", name="Delete").click()
    # expect(page.get_by_role("button", name="Delete")).to_be_visible()
    # page.get_by_role("button", name="Delete").click()
    # expect(page.locator("#create-page")).to_contain_text("Are you sure you want to delete your profile?")
    # page.get_by_role("link", name="GamesPlay").click()
    # page.get_by_role("link", name="Dashboard").click()
    # page.get_by_role("link", name="Create Game").click()
    
    
    
    