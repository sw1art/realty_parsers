import cianparser


def main_flat(citi):
    citi_parser = cianparser.CianParser(location=citi)
    data = citi_parser.get_flats(deal_type="sale", rooms=(1), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1})
    return data

def main_newobjects(citi):
    citi_parser = cianparser.CianParser(location=citi)
    data = citi_parser.get_newobjects(with_saving_csv=True)
    return data

def main_suburban(citi):
    citi_parser = cianparser.CianParser(location=citi)
    data = citi_parser.get_suburban(suburban_type="house",deal_type="sale", \
        with_saving_csv=True, \
        additional_settings={"start_page": 1, "end_page": 1, "sort_by":"price_from_min_to_max"})
    return data


if __name__ == "__main__":
    main_flat("Нижний Новгород")
    main_newobjects("Нижний Новгород")
    main_suburban("Нижний Новгород")