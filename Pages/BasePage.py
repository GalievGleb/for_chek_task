from playwright.sync_api import expect


class BasePage:
      __BASE_URL = 'https://www.saucedemo.com'

      def __init__(self, page):
          self.page = page
          self._endpoint = ''

      def full_url(self):
          return f"{self.__BASE_URL}/{self._endpoint}"

      def go_to_url(self):
          full_url = self.full_url()
          self.page.goto(self.full_url())
          self.page.wait_for_load_state('load')
          expect(self.page).to_have_url(full_url)

      def check_to_url(self):
          full_url = self.full_url()
          expect(self.page).to_have_url(full_url)

      def wait_for_selector_and_click(self, selector):
          self.page.wait_for_selector(selector)
          self.page.click(selector)


      def wait_for_selector_and_fill(self, selector, value):
          self.page.wait_for_selector(selector)
          self.page.type(selector, value)


      def wait_for_selector_and_visible(self, selector):
          self.page.wait_for_selector(selector)


      def wait_for_selector_enabled(self, selector):
          self.page.wait_for_selector(selector)
          self.page.is_visible(selector)