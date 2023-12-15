from playwright.sync_api import Page, expect
from playwright.async_api import async_playwright


def test_home_page_to_be_visible(page: Page) -> None:
    page.goto("localhost:3000/")
    expect(page).to_have_url("http://localhost:3000/")
    expect(page.locator("h1")).to_contain_text("GamesPlay")

    expect(page.get_by_role("navigation")).to_contain_text("Create Profile")
    expect(page.get_by_role("heading", name="ALL new games are")).to_be_visible()
    expect(page.get_by_role("heading", name="Only in GamesPlay")).to_be_visible()


def test_dashboard_to_be_visible(page: Page) -> None:
    page.goto("http://localhost:3000/profile/dashboard/")
    expect(page).to_have_url("http://localhost:3000/profile/dashboard/")


def test_create_user_profile(page: Page) -> None:
    page.goto("http://localhost:3000/profile/create/")
    expect(page).to_have_url("http://localhost:3000/profile/create/")
    page.get_by_label("Email:").click()
    page.get_by_label("Email:").fill("test@email.com")
    page.get_by_label("Age:").click()
    page.get_by_label("Age:").fill("66")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123456")
    page.get_by_role("button", name="Create Profile").press("Enter")

    expect(page).to_have_url("http://localhost:3000/profile/dashboard/")
    expect(page.get_by_role("paragraph")).to_contain_text("No games yet")

def test_profile_to_be_visible(page: Page) -> None:
    page.goto("http://localhost:3000/profile/details/")
    expect(page).to_have_url("http://localhost:3000/profile/details/")
    expect(page.locator("#game-details")).to_contain_text("Profile Details")
    expect(page.locator("#game-details")).to_contain_text("Edit")
    expect(page.locator("#game-details")).to_contain_text("Delete")

def test_edit_user_profile(page: Page) -> None:
    page.goto("http://localhost:3000/profile/edit/")
    expect(page).to_have_url("http://localhost:3000/profile/edit/")
    expect(page.locator("#register")).to_contain_text("Edit Profile")
    expect(page.get_by_role("button", name="Edit Profile")).to_be_visible()
    page.get_by_label("First Name:").click()
    page.get_by_label("First Name:").fill("Test")
    page.get_by_label("Last Name:").click()
    page.get_by_label("Last Name:").fill("User")
    page.get_by_label("Profile Picture:").click()
    page.get_by_label("Profile Picture:").fill("https://static.vecteezy.com/system/resources/thumbnails/019/900/322/small/happy-young-cute-illustration-face-profile-png.png")
    page.get_by_role("button", name="Edit Profile").click()
    expect(page).to_have_url("http://localhost:3000/profile/details/")
    expect(page.locator("#game-details")).to_contain_text("Test User")
    expect(page.get_by_role("img", name="profile-image")).to_be_visible()
    

def test_create_game_to_be_visible(page: Page) -> None:
    page.goto("http://localhost:3000/game/create/")
    expect(page).to_have_url("http://localhost:3000/game/create/")
    expect(page.get_by_role("button", name="Create Game")).to_be_visible()

def test_create_game_Amazon_Crucible_with_credentials(page: Page) -> None:
    page.goto("http://localhost:3000/game/create/")
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("Amazon Crucible")
    page.get_by_label("Category:").click()
    page.get_by_label("Category:").select_option("Action")
    page.get_by_label("Rating:").click()
    page.get_by_label("Rating:").fill("5")
    page.get_by_label("Max level:").click()
    page.get_by_label("Max level:").fill("10")
    page.get_by_label("Image url:").click()
    page.get_by_label("Image url:").fill("https://ichef.bbci.co.uk/news/976/cpsprodpb/13729/production/_112375697_1331db7a-17c0-4401-8cac-6a2309ff49b6.jpg")
    page.get_by_label("Summary:").click()
    page.get_by_label("Summary:").fill("Amazon Crucible: 'Can games be as fun to watch as they are to play?'Crucible is a new free-to-play PC game and is a competitive shooting title that's a cross between Overwatch, Gears of War and League of Legends.")
    page.get_by_role("button", name="Create Game").press("Enter")
    expect(page).to_have_url("http://localhost:3000/profile/dashboard/")

def test_create_game_Red_Dead_Redemption_2_with_credentials(page: Page) -> None:
    page.goto("http://localhost:3000/game/create/")
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("Red Dead Redemption 2")
    page.get_by_label("Category:").click()
    page.get_by_label("Category:").select_option("Adventure")
    page.get_by_label("Rating:").click()
    page.get_by_label("Rating:").fill("5")
    page.get_by_label("Max level:").click()
    page.get_by_label("Max level:").fill("21")
    page.get_by_label("Image url:").click()
    page.get_by_label("Image url:").fill("https://assets1.ignimgs.com/2018/06/13/drifter-combat-1528858751329.jpg")
    page.get_by_label("Summary:").click()
    page.get_by_label("Summary:").fill("Arthur Morgan`s sprawling tale of loyalty, conviction, and the price of infamy is only the beginning of Red Dead Redemption 2. The marvelous PC port overhauled and further enhanced the gorgeous wild western atmosphere of Rockstar's most recent open-world adventure and added even more activities, unlockables, and impossibly fine details to its expansive map. It's possibly one of the biggest and best single-player PC games ever and it has an extensive multiplayer mode too.")
    page.get_by_role("button", name="Create Game").press("Enter")
    expect(page).to_have_url("http://localhost:3000/profile/dashboard/")
    
def test_create_game_Forza_Horizon_5_with_credentials(page: Page) -> None:
    page.goto("http://localhost:3000/game/create/")
    page.get_by_label("Title:").click()
    page.get_by_label("Title:").fill("Forza Horizon 5")
    page.get_by_label("Category:").click()
    page.get_by_label("Category:").select_option("Action")
    page.get_by_label("Rating:").click()
    page.get_by_label("Rating:").fill("4")
    page.get_by_label("Max level:").click()
    page.get_by_label("Max level:").fill("10")
    page.get_by_label("Image url:").click()
    page.get_by_label("Image url:").fill("https://assets2.ignimgs.com/2012/09/19/ftl23jpg-4415ef.jpg")
    page.get_by_label("Summary:").click()
    page.get_by_label("Summary:").fill("Driving games are a long-running, important, and respected force in the story of video games, but it takes a special one to completely seize the imaginations of both the car-obsessed and the automotively illiterate so successfully. By that measure, Forza Horizon 5 is truly special. A slick and speedy smorgasbord of total driving freedom built on the back of what`s already been the open-world racing series to beat for nearly a decade, Forza Horizon 5 broke through in a way not even its excellent predecessors managed.")
    page.get_by_role("button", name="Create Game").press("Enter")
    expect(page).to_have_url("http://localhost:3000/profile/dashboard/")

   
def test_delete_user_profile(page: Page) -> None:
    page.goto("http://localhost:3000/profile/details/")
    page.get_by_role("link", name="Delete").click()
    expect(page.locator("#create-page")).to_contain_text("Are you sure you want to delete your profile?")
    expect(page.get_by_role("button")).to_contain_text("Delete")
    expect(page.get_by_role("button", name="Delete")).to_be_visible()
    page.get_by_role("button", name="Delete").click()
    expect(page).to_have_url("http://localhost:3000/")
    expect(page.get_by_role("heading", name="ALL new games are")).to_be_visible()
    expect(page.get_by_role("heading", name="Only in GamesPlay")).to_be_visible()
    
    