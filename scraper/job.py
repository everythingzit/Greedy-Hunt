class Job:
    def __init__(self, title, company, location, url, date_posted):
        self.title = title
        self.company = company
        self.location = location
        self.url = url
        self.date_posted = date_posted

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def date_posted(self):
        return self._date_posted

    @date_posted.setter
    def date_posted(self, value):
        self._date_posted = value