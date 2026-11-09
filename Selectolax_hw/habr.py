from pprint import pprint

from httpx import Client
from selectolax.parser import HTMLParser, Node

URL = "https://habr.com/ru/search/page2/?q={%D0%A2%D1%83%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB}+Python&target_type=posts&order=date"
# "https://habr.com/ru/articles/"
ARTICLES_LIST = ".tm-page__main_has-sidebar.tm-page__main"
ARTICLE_ELEMENT = ".tm-article-snippet.tm-article-snippet"
POST_AUTHOR_ELEMENT = ".tm-user-info__username"
POST_LINK_ELEMENT = ".tm-title__link"
POST_SNIPPET_ELEMENT = ".article-formatted-body.article-formatted-body.article-formatted-body_version-2"
TUTORIAL = ".tm-publication-label.tm-publication-label_variant-tutorial"


def parse_articles() -> dict[int, dict[str, str]]:
    articles = {}

    response = Client().get(url=URL)

    tree = HTMLParser(html=response.text)

    articles_list = tree.css_first(ARTICLES_LIST)

    for num, article in enumerate(articles_list.css(ARTICLE_ELEMENT), start=1):  # type: ignore
        author: Node = article.css_first(POST_AUTHOR_ELEMENT)  # type: ignore
        author_name: str = author.text()  # type: ignore
        author_link: str = author.attributes.get("href")  # type: ignore

        post: Node = article.css_first(POST_LINK_ELEMENT)  # type: ignore
        post_title: str = post.text()  # type: ignore
        post_link: str = post.attributes.get("href")  # type: ignore

        post_snippet: str = article.css_first(POST_SNIPPET_ELEMENT).text()  # type: ignore

        tutorial: bool = bool(tree.css_first(TUTORIAL))

        articles[num] = {
            "author": author_name,
            "author_link": author_link,
            "post_title": post_title,
            "post_link": post_link,
            "post_snippet": post_snippet,
            "tutorial": tutorial,
        }

    return articles


if __name__ == "__main__":
    pprint(parse_articles())
