from backend.src.services import emoji_counter

definition = {
    'type': 'Page',
    'description': 'Collects the webpage head title and meta info',
    'score': 0,
    'url_score': 0,
    'title_score': 40,
    'description_score': 50,
    'author_score': 40,
    'author_twitter_score': 50,
    'publication_score': 40,
    'publication_twitter_score': 50,
    'image_alt_score': 40,
    'topics_score': 0,
    'image_src_score': 0,
    'score description': 'Each element of the website scraping gets a predefined score (the ones that are presented above) and is further used to evaluate the tweets',
    'notes': 'The page getter is being scored based on the amount and type of data the website contains. The more data the better the score.'
}


wanted_meta = [{'tag_name': ['meta_twitter:domain', 'meta_og:url'], 'item_name': 'shorturl', 'score': definition['url_score']},
               {'tag_name': ['meta_twitter:title', 'meta_og:title', 'meta_title'], 'item_name': 'title', 'score': definition["title_score"]},
               {'tag_name': ['meta_twitter:description', 'meta_twitter:image:alt', 'meta_og:description', 'meta_description'],
                'item_name': 'description', 'score': definition["description_score"]},
               {'tag_name': ['meta_og:author', 'meta_article:author'], 'item_name': 'author',
                'score': definition["author_score"]},
               {'tag_name': ['meta_twitter:creator'], 'item_name': 'author_twitter',
                'score': definition["author_twitter_score"]},
               {'tag_name': ['meta_og:site_name'], 'item_name': 'publication',
                'score': definition["publication_score"]},
               {'tag_name': ['meta_twitter:site'], 'item_name': 'publication_twitter',
                'score': definition["publication_twitter_score"]},
               {'tag_name': ['meta_twitter:image:alt'], 'item_name': 'image_alt',
                'score': definition["image_alt_score"]},
               {'tag_name': ['meta_news_keywords'], 'item_name': 'topics', 'score': definition["topics_score"]},
               {'tag_name': ['meta_twitter:image:src', 'meta_twitter:image', 'meta_og:image'], 'item_name': 'image_src', 'score': definition["image_src_score"]}]


def get_meta_tags(source):
    meta_tags = {}

    if source.title:
        meta_tags["meta_title"] = source.title.text

    for tag in source.find_all("meta"):
        if tag.get("property", None) and tag.get("content", None):
            meta_tags["meta_" + str(tag.get("property", None))] = tag.get("content", None)

        if tag.get("name", None) and tag.get("content", None):
            meta_tags["meta_" + str(tag.get("name", None))] = tag.get("content", None)

    return meta_tags


def get_page_details(soup):
    result = [definition]

    meta_tags = get_meta_tags(soup)

    for item in wanted_meta:
        for tag in item['tag_name']:
            if tag in meta_tags.keys():
                result.append({item['item_name']: meta_tags[tag], 'score': item['score'], 'notes': ''})
                break

    for item in result[1:]:
        if 'author' in item.keys():
            if item['author'].startswith('https:') or item['author'].startswith('http:'):
                result.pop(result.index(item))

        elif 'author_twitter' in item.keys():
            if item['author_twitter'].startswith('https:') or item['author_twitter'].startswith('http:'):
                 twitter_creator = '@' + str(item['item_name'].rsplit('/', 1)[-1])
                 item['author_twitter'] = '@' + twitter_creator

    return result