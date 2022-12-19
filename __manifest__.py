{
    "name": "Odoo JS",
    "summary": "Odoo JavaScript",
    "version": "0.1.0",
    "category": "Services",
    "author": "Demelash Kasaye",
    "website": "https://demelashkasaye.com",
    "application": True,
    'sequence': -10,
    "depends": [
        "base",
        "website",

    ],
    "data": [
        "views/assets.xml",
        "views/website_form.xml",
    ]
}
