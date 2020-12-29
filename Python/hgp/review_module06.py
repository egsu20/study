# 외부 모듈(geopy - 주소) 사용하기
# cmd 에서 pip install geopy
# 삭제 시 pip uninstall geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="JISU")
location = geolocator.geocode("175 5th Avenue NYC")
print(location)
print()

location = geolocator.geocode("Seoul, South Korea")
print(location)
print(location.latitude)
print(location.longitude)
print(location.raw)