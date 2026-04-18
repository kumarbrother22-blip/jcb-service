from urllib.parse import quote

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure value

BUSINESS_INFO = {
    "name": "Aman Trading JCB Service",
    "tagline": "Reliable earthmoving support for residential, commercial, and industrial projects.",
    "phone_display": "+91 91770 34464",
    "phone_href": "tel:+919177034464",
    "whatsapp_number": "919177034464",
    "email": "hello@amantradingjcbservice.in",
    "location": "Serving Bihar Lalpur and surrounding areas",
    "hours": "Monday to Sunday, 6:00 AM to 9:00 PM",
}

WHATSAPP_MESSAGE = (
    "Hello Aman Trading JCB Service, I need JCB support for my project. "
    "Please share availability and pricing."
)

SERVICE_GROUPS = [
    {
        "title": "Excavation and site preparation",
        "description": "For foundations, pits, trenches, and early-stage land work that needs careful machine handling.",
        "jobs": ["Plot excavation", "Foundation digging", "Site clearing", "Debris removal"],
    },
    {
        "title": "Construction support",
        "description": "For active building sites that need dependable machine support to keep work moving.",
        "jobs": ["Material loading", "Backfilling", "Road work support", "Utility trenching"],
    },
    {
        "title": "Land and access improvements",
        "description": "For farms, private land, and commercial spaces that need leveling, grading, or access preparation.",
        "jobs": ["Land leveling", "Approach road preparation", "Drainage channels", "Boundary cleanup"],
    },
]

TRUST_HIGHLIGHTS = [
    "Experienced operators focused on safe machine handling",
    "Responsive support for urgent and planned job work",
    "Clear communication on site timing and job scope",
    "Well-maintained equipment ready for varied ground conditions",
]

GALLERY_ITEMS = [
    {
        "filename": "jcb-excavators-real.jpg",
        "title": "JCB excavators on an active site",
        "caption": "Real project-site machinery supporting excavation work at a live construction area.",
        "author": "Tiia Monto",
        "source_url": "https://commons.wikimedia.org/wiki/File:JCB_excavators.jpg",
        "license_name": "CC BY-SA 4.0",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    },
    {
        "filename": "jcb-excavator-real.jpg",
        "title": "JCB excavator at work",
        "caption": "A real JCB excavator in action, matching the type of earthmoving support offered on site.",
        "author": "Putevik",
        "source_url": "https://commons.wikimedia.org/wiki/File:JCB_Excavator.jpg",
        "license_name": "CC BY-SA 4.0",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    },
    {
        "filename": "jcb-backhoe-loader-real.jpg",
        "title": "Indian JCB backhoe loader",
        "caption": "A real JCB backhoe-loader similar to the machine customers commonly use for digging and loading work.",
        "author": "Arjun Sinh Jadeja",
        "source_url": "https://commons.wikimedia.org/wiki/File:Jcb.backhoe-loader.jpg",
        "license_name": "CC BY-SA 4.0",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    },
]


def build_whatsapp_link(message=WHATSAPP_MESSAGE):
    return f"https://wa.me/{BUSINESS_INFO['whatsapp_number']}?text={quote(message)}"


@app.context_processor
def inject_site_data():
    return {
        "business": BUSINESS_INFO,
        "service_groups": SERVICE_GROUPS,
        "trust_highlights": TRUST_HIGHLIGHTS,
        "whatsapp_link": build_whatsapp_link(),
    }


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', gallery_items=GALLERY_ITEMS)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        _ = (email, message)
        flash(
            f"Thank you, {name}! We received your enquiry and will contact you soon.",
            'success'
        )
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
