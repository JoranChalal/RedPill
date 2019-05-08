from ..models import Location

def filter_unsual_locations_from_postal_code(postal_code):
    pass

def get_mean_price_by_square_from_postal_code(postal_code):
    locations = Location.objects.filter(postal_code=postal_code, has_been_seen=True, is_relevant=True)

    mean_by_square = 0
    count = 0
    for location in locations:
        mean_by_square += (location.price / location.square)
        count += 1
    mean_by_square = mean_by_square / count

    return float(str(round(mean_by_square, 2)))