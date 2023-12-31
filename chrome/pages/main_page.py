"""This module represents main page."""
from chrome.locators.main_page_locators import MainPageLocators
from chrome.pages.base_page import BasePage


class MainPage(BasePage):
    """Main page."""
    locators = MainPageLocators()

    def add_post(self, title: str, description: str, content: str):
        self.element_is_clickable(locator=self.locators.ADD_POST_BUTTON).click()

        self.element_is_visible(
            self.format_locator(
                locator=self.locators.XPATH_CONTAINS_DYNAMIC,
                text='Create Post'
            )
        )

        self.element_is_clickable(locator=self.locators.INPUT_TITLE).send_keys(title)

        self.element_is_clickable(locator=self.locators.INPUT_DESCRIPTION).send_keys(description)

        self.element_is_clickable(locator=self.locators.INPUT_CONTENT).send_keys(content)

        self.element_is_clickable(locator=self.locators.SAVE_BUTTON).click()

        self.element_is_visible(locator=self.locators.POST_IMAGE)

    def go_to_all_posts(self):
        self.element_is_clickable(
            locator=self.format_locator(
                locator=self.locators.XPATH_CONTAINS_DYNAMIC,
                text='Home'
            )
        ).click()

        self.element_is_visible(locator=self.locators.POST_CARD)

    def is_post_with_title_visible_in_all_posts(self, title: str) -> bool:
        return self.is_element_visible(
            locator=self.format_locator(
                locator=self.locators.POST_TITLE_LOCATOR,
                text=title
            )
        )

    def open_contact_us_page(self):
        self.element_is_clickable(
            locator=self.locators.CONTACT_TAB
        ).click()

        self.element_is_visible(
            locator=self.format_locator(
                locator=self.locators.XPATH_CONTAINS_DYNAMIC,
                text='Contact us!'
            )
        )