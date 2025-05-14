import folium

# 데이터 설정
locations = [
    {
        "country": "United States",
        "lat": 38.9072,
        "lng": -77.0369,
        "habitatPresence": True,
        "description": "Large-scale Habitat projects across many states."
    },
    {
        "country": "Brazil",
        "lat": -15.7939,
        "lng": -47.8828,
        "habitatPresence": True,
        "description": "Multiple urban and rural housing programs."
    },
    {
        "country": "India",
        "lat": 20.5937,
        "lng": 78.9629,
        "habitatPresence": True,
        "description": "Focus on sanitation and affordable housing."
    },
    {
        "country": "Germany",
        "lat": 51.1657,
        "lng": 10.4515,
        "habitatPresence": False,
        "description": "Local NGOs provide non-loan based housing support."
    },
    {
        "country": "Japan",
        "lat": 36.2048,
        "lng": 138.2529,
        "habitatPresence": False,
        "description": "High vacancy rates addressed by government subsidies."
    },
    {
        "country": "Portugal",
        "lat": 39.3999,
        "lng": -8.2245,
        "habitatPresence": False,
        "description": "Vacant housing reuse led by municipalities."
    }
]

# 지도 생성
habitat_map = folium.Map(location=[20, 0], zoom_start=2)

# 마커 추가
for loc in locations:
    popup_text = f"""
    <strong>{loc['country']}</strong><br>
    {loc['description']}<br>
    Habitat presence: {'Yes' if loc['habitatPresence'] else 'No'}
    """
    folium.Marker(
        location=[loc['lat'], loc['lng']],
        popup=popup_text,
        icon=folium.Icon(color='green' if loc['habitatPresence'] else 'gray')
    ).add_to(habitat_map)

# HTML 파일로 저장
habitat_map.save('habitat_vs_ngos_map.html')
import folium

# 데이터 설정
locations = [
    {
        "country": "United States",
        "lat": 38.9072,
        "lng": -77.0369,
        "habitatPresence": True,
        "description": "Large-scale Habitat projects across many states."
    },
    {
        "country": "Brazil",
        "lat": -15.7939,
        "lng": -47.8828,
        "habitatPresence": True,
        "description": "Multiple urban and rural housing programs."
    },
    {
        "country": "India",
        "lat": 20.5937,
        "lng": 78.9629,
        "habitatPresence": True,
        "description": "Focus on sanitation and affordable housing."
    },
    {
        "country": "Germany",
        "lat": 51.1657,
        "lng": 10.4515,
        "habitatPresence": False,
        "description": "Local NGOs provide non-loan based housing support."
    },
    {
        "country": "Japan",
        "lat": 36.2048,
        "lng": 138.2529,
        "habitatPresence": False,
        "description": "High vacancy rates addressed by government subsidies."
    },
    {
        "country": "Portugal",
        "lat": 39.3999,
        "lng": -8.2245,
        "habitatPresence": False,
        "description": "Vacant housing reuse led by municipalities."
    }
]

# 지도 생성
habitat_map = folium.Map(location=[20, 0], zoom_start=2)

# 마커 추가
for loc in locations:
    popup_text = folium.Popup(
        html=f"""
        <div>
            <strong>{loc['country']}</strong><br>
            {loc['description']}<br>
            Habitat presence: {'Yes' if loc['habitatPresence'] else 'No'}
        </div>
        """,
        max_width=250
    )
    marker_icon = folium.Icon(color='green' if loc['habitatPresence'] else 'gray')
    folium.Marker(
        location=[loc['lat'], loc['lng']],
        popup=popup_text,
        icon=marker_icon
    ).add_to(habitat_map)

# HTML 파일로 저장
habitat_map.save('habitat_vs_ngos_map.html')