# app.py
"""Flask MVC demo for MZPets – controller / entry‑point."""

from flask import Flask, render_template, request, redirect, url_for
from models import Pet, Service, Testimonial, TeamMember

app = Flask(__name__)

# ── Sample data ──────────────────────────────────────────────

pets = [
    Pet(name="Buddy",   species="Dog",   image_url="https://placedog.net/400/280?id=1",   description="Friendly golden retriever, loves fetch and long walks."),
    Pet(name="Luna",    species="Cat",   image_url="https://placekitten.com/400/280",      description="Calm tabby with the softest fur you'll ever touch."),
    Pet(name="Max",     species="Dog",   image_url="https://placedog.net/400/280?id=3",   description="Energetic husky puppy ready for adventure."),
    Pet(name="Cleo",    species="Cat",   image_url="https://placekitten.com/401/280",      description="Playful Siamese who loves to cuddle on your lap."),
    Pet(name="Kiwi",    species="Bird",  image_url="https://via.placeholder.com/400x280/FFF3E0/E67E22?text=🦜+Kiwi", description="Colourful budgie that can whistle three songs."),
    Pet(name="Shelly",  species="Other", image_url="https://via.placeholder.com/400x280/FFF3E0/E67E22?text=🐢+Shelly", description="Gentle tortoise, easy to care for, lives for decades."),
    Pet(name="Daisy",   species="Dog",   image_url="https://placedog.net/400/280?id=5",   description="Sweet beagle with an incredible nose for treats."),
    Pet(name="Milo",    species="Cat",   image_url="https://placekitten.com/402/280",      description="Ginger kitten with endless energy and curiosity."),
]

featured_pets = pets[:4]

services = [
    Service(name="Pet Adoption",  description="Find your perfect companion from our responsibly‑sourced animals.",       icon="🏠"),
    Service(name="Grooming",      description="Professional bathing, trimming, and styling for dogs and cats.",          icon="✂️"),
    Service(name="Nutrition",     description="Premium food brands and personalised diet plans for every breed.",        icon="🥗"),
    Service(name="Accessories",   description="Toys, beds, leashes, and everything your pet could ever need.",           icon="🎾"),
    Service(name="Vet Check‑ups", description="On‑site veterinary consultations, vaccinations, and health screenings.", icon="🩺"),
    Service(name="Training",      description="Obedience classes and behavioural workshops for puppies and adults.",     icon="🎓"),
]

testimonials = [
    Testimonial(quote="MZPets helped us find the perfect puppy for our family. The team was incredibly patient and caring.", author="Sarah M."),
    Testimonial(quote="Best grooming service in town! Buddy always comes out looking like a show dog.", author="James K."),
    Testimonial(quote="Their nutrition advice transformed our cat's health. Highly recommended!", author="Priya R."),
]

team = [
    TeamMember(name="Maria Zulu",  role="Founder & CEO",        emoji="👩‍💼"),
    TeamMember(name="David Park",  role="Head Veterinarian",     emoji="👨‍⚕️"),
    TeamMember(name="Lena Torres", role="Grooming Specialist",   emoji="💇‍♀️"),
    TeamMember(name="Sam Okonkwo", role="Adoption Coordinator",  emoji="🤝"),
]


# ── Routes (controllers) ────────────────────────────────────

@app.route("/")
def home():
    return render_template(
        "home.html",
        featured_pets=featured_pets,
        services=services,
        testimonials=testimonials,
    )


@app.route("/about")
def about():
    return render_template("about.html", team=team)


@app.route("/services")
def services_page():
    return render_template("services.html", services=services)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html", pets=pets)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def contact_submit():
    name    = request.form.get("name", "Friend")
    email   = request.form.get("email", "")
    subject = request.form.get("subject", "")
    message = request.form.get("message", "")
    # In a real app you'd save this or send an email.
    return render_template("thank_you.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)
