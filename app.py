import streamlit as st
import backend

backend.MovieData()

st.title("Online Movie Ticket Booking System")

# Initialize session state variables if they do not exist
if "Movie_ID" not in st.session_state:
    st.session_state["Movie_ID"] = ""
if "Movie_Name" not in st.session_state:
    st.session_state["Movie_Name"] = ""
if "Release_Date" not in st.session_state:
    st.session_state["Release_Date"] = ""
if "Director" not in st.session_state:
    st.session_state["Director"] = ""
if "Cast" not in st.session_state:
    st.session_state["Cast"] = ""
if "Budget" not in st.session_state:
    st.session_state["Budget"] = ""
if "Duration" not in st.session_state:
    st.session_state["Duration"] = ""
if "Rating" not in st.session_state:
    st.session_state["Rating"] = ""

# Input fields
Movie_ID = st.text_input("Movie ID", value=st.session_state["Movie_ID"])
Movie_Name = st.text_input("Movie Name", value=st.session_state["Movie_Name"])
Release_Date = st.text_input("Release Date", value=st.session_state["Release_Date"])
Director = st.text_input("Director", value=st.session_state["Director"])
Cast = st.text_input("Cast", value=st.session_state["Cast"])
Budget = st.text_input("Budget (Crores INR)", value=st.session_state["Budget"])
Duration = st.text_input("Duration (Hrs)", value=st.session_state["Duration"])
Rating = st.text_input("Rating (Out of 5)", value=st.session_state["Rating"])

# Functions
def clear_inputs():
    st.session_state["Movie_ID"] = ""
    st.session_state["Movie_Name"] = ""
    st.session_state["Release_Date"] = ""
    st.session_state["Director"] = ""
    st.session_state["Cast"] = ""
    st.session_state["Budget"] = ""
    st.session_state["Duration"] = ""
    st.session_state["Rating"] = ""

def add_movie():
    if Movie_ID and Movie_Name:
        backend.AddMovieRec(Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
        st.success(f"Added Movie: {Movie_Name}")
        clear_inputs()

def display_movies():
    movies = backend.ViewMovieData()
    for movie in movies:
        st.write(movie)

def search_movie():
    results = backend.SearchMovieData(st.session_state["Movie_ID"], st.session_state["Movie_Name"], st.session_state["Release_Date"], st.session_state["Director"], st.session_state["Cast"], st.session_state["Budget"], st.session_state["Duration"], st.session_state["Rating"])
    for result in results:
        st.write(result)

def update_movie(selected_id):
    if selected_id and Movie_ID and Movie_Name:
        backend.UpdateMovieData(selected_id, Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating)
        st.success(f"Updated Movie ID: {selected_id}")

def delete_movie(selected_id):
    if selected_id:
        backend.DeleteMovieRec(selected_id)
        st.success(f"Deleted Movie ID: {selected_id}")

# Buttons
if st.button("Add Movie"):
    add_movie()

if st.button("Display Movies"):
    display_movies()

if st.button("Search Movies"):
    search_movie()

# Selectbox for updating and deleting movies
all_movies = backend.ViewMovieData()
movie_options = {f"{movie[0]} - {movie[2]}": movie[0] for movie in all_movies}
selected_movie = st.selectbox("Select a Movie to Update/Delete", options=list(movie_options.keys()))

if selected_movie:
    selected_id = movie_options[selected_movie]
    if st.button("Update Movie"):
        update_movie(selected_id)

    if st.button("Delete Movie"):
        delete_movie(selected_id)