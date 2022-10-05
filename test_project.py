import pytest
import project.project as project


def test_PI_request():
    with pytest.raises(ValueError):
        assert project.API_request("5") is True

    with pytest.raises(ValueError):
        assert project.API_request("TV") is True

    with pytest.raises(ValueError):
        assert project.API_request("MOVIE") is True


def test_image_scrape():
    with pytest.raises(ValueError):
        assert project.image_scrape("5", 0) is True

    with pytest.raises(ValueError):
        assert project.image_scrape("", "movie") is True

    with pytest.raises(ValueError):
        assert project.image_scrape("", "") is True