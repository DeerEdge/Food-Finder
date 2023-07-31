"""
ScatterplotLayer
================

Plot of the number of exits for various subway stops within San Francisco, California.

Adapted from the deck.gl documentation.
"""

import streamlit as st
import pydeck as pdk
import pandas as pd
from django_api.models import Entity, Producer

data = []

all_entities = Entity.objects.all()
for entity in all_entities:
    entity_producer = Producer.objects.filter(entity=entity).first()
    new_data = {'name': entity.user.first_name,
        'latitude': float(entity.latitude),
        'longitude': float(entity.longitude),
        'description': entity_producer.description}

    data.append(new_data)


# Define a layer to display on a map
layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    get_radius=1000,
    radius_scale=6,
    radius_min_pixels=1,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position=["longitude", "latitude"],
    get_fill_color=[255, 140, 0],
    get_line_color=[0, 0, 0],
)

# Set the viewport location
#view_state = pdk.ViewState(latitude=37.7749295, longitude=-122.4194155, zoom=10, bearing=0, pitch=0)

# Render
r = pdk.Deck(layers=[layer], tooltip={"text": "{name}"})
st.pydeck_chart(r)
