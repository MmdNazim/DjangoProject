from django.shortcuts import render
from datetime import datetime, timedelta


def home(request):
    categories = [
        {"icon": "https://placehold.co/100x100", "name": "Electronics"},
        {"icon": "https://placehold.co/100x100", "name": "Fashion"},
        {"icon": "https://placehold.co/100x100", "name": "Home & Living"},
        {"icon": "https://placehold.co/100x100", "name": "Toys & Kids"},
        {"icon": "https://placehold.co/100x100", "name": "Beauty & Personal Care"},
        {"icon": "https://placehold.co/100x100", "name": "Groceries"},
        {"icon": "https://placehold.co/100x100", "name": "Computers"},
        {"icon": "https://placehold.co/100x100", "name": "Books"},
        {"icon": "https://placehold.co/100x100", "name": "Footwear"},
        {"icon": "https://placehold.co/100x100", "name": "Watches & Accessories"}
    ]

    FeaturedProductsList = [
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Wireless+Charger",
            "title": "Wireless Charger",
            "price": "$29.99",
            "review_count": 128,
            "rating": 4.5
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Bluetooth+Speaker",
            "title": "Bluetooth Speaker",
            "price": "$49.99",
            "review_count": 256,
            "rating": 4.7
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Smart+Watch",
            "title": "Smart Watch",
            "price": "$99.99",
            "review_count": 412,
            "rating": 4.8
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Power+Bank",
            "title": "Power Bank",
            "price": "$19.99",
            "review_count": 89,
            "rating": 4.3
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Headphones",
            "title": "Wireless Headphones",
            "price": "$59.99",
            "review_count": 304,
            "rating": 4.6
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Keyboard",
            "title": "Mechanical Keyboard",
            "price": "$79.99",
            "review_count": 142,
            "rating": 4.4
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Mouse",
            "title": "Gaming Mouse",
            "price": "$24.99",
            "review_count": 221,
            "rating": 4.5
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=USB-C+Cable",
            "title": "USB-C Fast Cable",
            "price": "$9.99",
            "review_count": 67,
            "rating": 4.2
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Earbuds",
            "title": "Wireless Earbuds",
            "price": "$39.99",
            "review_count": 387,
            "rating": 4.7
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Webcam",
            "title": "HD Webcam",
            "price": "$34.99",
            "review_count": 178,
            "rating": 4.5
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Charger+Adapter",
            "title": "Fast Charger Adapter",
            "price": "$14.99",
            "review_count": 94,
            "rating": 4.1
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Laptop+Stand",
            "title": "Aluminum Laptop Stand",
            "price": "$27.99",
            "review_count": 133,
            "rating": 4.4
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Hard+Drive",
            "title": "External Hard Drive",
            "price": "$89.99",
            "review_count": 512,
            "rating": 4.8
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Flash+Drive",
            "title": "128GB Pen Drive",
            "price": "$12.99",
            "review_count": 76,
            "rating": 4.2
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Phone+Case",
            "title": "Shockproof Phone Case",
            "price": "$9.49",
            "review_count": 210,
            "rating": 4.6
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Tripod",
            "title": "Portable Tripod",
            "price": "$22.99",
            "review_count": 144,
            "rating": 4.3
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=LED+Light",
            "title": "LED Ring Light",
            "price": "$18.99",
            "review_count": 177,
            "rating": 4.5
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Tablet+Stand",
            "title": "Adjustable Tablet Stand",
            "price": "$16.99",
            "review_count": 68,
            "rating": 4.1
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=VR+Headset",
            "title": "VR Headset",
            "price": "$149.99",
            "review_count": 299,
            "rating": 4.7
        },
        {
            "image": "https://placehold.co/300x300/f5f5f5/a3a3a3?text=Smart+Bulb",
            "title": "Smart LED Bulb",
            "price": "$11.99",
            "review_count": 123,
            "rating": 4.3
        }
    ]
    context = {'categories': categories, 'FeaturedProductsList':FeaturedProductsList}
    return render(request, 'index.html', context)



def product(request):


    CustomerReviewsList = [
        {
            "name": "Emily Rodriguez",
            "rating": 5,
            "date": "November 5, 2024",
            "comment": "Perfect for my daily commute! The ANC blocks out all the subway noise. Sound quality is crystal clear and the design is sleek. Worth every penny."
        },
        {
            "name": "James Walker",
            "rating": 4,
            "date": "October 28, 2024",
            "comment": "Very comfortable to wear for long hours. Battery life is impressive, but the price feels a bit high."
        },
        {
            "name": "Ayesha Khan",
            "rating": 5,
            "date": "October 15, 2024",
            "comment": "Amazing sound quality and premium build. Noise cancellation works great even in busy environments."
        },
        {
            "name": "Daniel Smith",
            "rating": 3,
            "date": "September 30, 2024",
            "comment": "Sound is good, but Bluetooth connection sometimes drops. Could be improved with updates."
        },
        {
            "name": "Rahul Mehta",
            "rating": 4,
            "date": "September 20, 2024",
            "comment": "Great headphones for work and travel. Comfortable cushions and clear audio."
        },
        {
            "name": "Sophia Lee",
            "rating": 5,
            "date": "September 10, 2024",
            "comment": "Absolutely love these headphones! Stylish, lightweight, and excellent noise cancellation."
        },
        {
            "name": "Michael Brown",
            "rating": 4,
            "date": "August 29, 2024",
            "comment": "Good overall performance. Bass is strong and battery easily lasts a full day."
        },
        {
            "name": "Fatima Noor",
            "rating": 5,
            "date": "August 18, 2024",
            "comment": "Best headphones I’ve owned so far. Perfect balance between comfort and sound quality."
        },
        {
            "name": "Chris Johnson",
            "rating": 3,
            "date": "August 5, 2024",
            "comment": "Decent sound, but expected better noise cancellation at this price point."
        },
        {
            "name": "Nusrat Jahan",
            "rating": 4,
            "date": "July 25, 2024",
            "comment": "Very good for online meetings and music. Mic quality is clear and reliable."
        }
    ]

    RelatedProductsList = [
        {
            "title": "Wireless Earbuds Pro",
            "rating": 5,
            "price": 89.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Noise Cancelling Headphones",
            "rating": 4,
            "price": 149.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Bluetooth Speaker Mini",
            "rating": 4,
            "price": 59.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Gaming Headset X",
            "rating": 5,
            "price": 129.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Studio Monitor Headphones",
            "rating": 3,
            "price": 99.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Wireless Neckband",
            "rating": 4,
            "price": 39.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Portable Bluetooth Speaker",
            "rating": 5,
            "price": 79.99,
            "image": "https://placehold.co/200x200"
        },
        {
            "title": "Over-Ear Comfort Headphones",
            "rating": 4,
            "price": 109.99,
            "image": "https://placehold.co/200x200"
        }
    ]

    ProductSpecificationList = {
        "Brand": "AudioTech Pro",
        "Model": "AT-WH3000",
        "Material": "Aluminum & Leather",
        "Weight": "250g",
        "Warranty": "2 Years",
        "Color": "Midnight Black"
        }

    context = {'CustomerReviewsList': CustomerReviewsList, 'RelatedProductsList': RelatedProductsList, 'ProductSpecificationList': ProductSpecificationList}
    return render(request, 'product.html', context)

def cart(request):
    CartList = [
        {
            "name": "Wireless Headphones",
            "description": "Premium sound quality",
            "price": 79.99,
            "quantity": 1,
            "image": "https://placehold.co/120x120"
        },
        {
            "name": "Bluetooth Speaker",
            "description": "Deep bass and portable design",
            "price": 49.99,
            "quantity": 2,
            "image": "https://placehold.co/120x120"
        },
        {
            "name": "Noise Cancelling Earbuds",
            "description": "Crystal clear calls",
            "price": 59.99,
            "quantity": 1,
            "image": "https://placehold.co/120x120"
        },
        {
            "name": "Gaming Headset",
            "description": "Immersive surround sound",
            "price": 99.99,
            "quantity": 1,
            "image": "https://placehold.co/120x120"
        },
        {
            "name": "Smart Watch",
            "description": "Fitness and health tracking",
            "price": 129.99,
            "quantity": 1,
            "image": "https://placehold.co/120x120"
        }
    ]

    OrderSummary = {
    "subtotal": 429.96,
    "shipping": 15.00,
    "tax": 35.50,
    "total": 480.46
}

    context = {'CartList': CartList, 'OrderSummary': OrderSummary}
    return render(request, 'cart.html', context)

def checkout(request):

    PaymentMethod = {
        "card": "Credit/Debit Card",
        "cod": "Cash on Delivery (COD)",
        "paypal": "PayPal",
        "stripe": "Stripe"
    }

    OrderSummaryList = [
        {
            "image": "https://placehold.co/60x60/f5f5f5/a3a3a3",
            "name": "Wireless Headphones",
            "quantity": 1,
            "price": 79.99
        },
        {
            "image": "https://placehold.co/60x60/f5f5f5/a3a3a3",
            "name": "Bluetooth Speaker",
            "quantity": 2,
            "price": 129.98
        },
        {
            "image": "https://placehold.co/60x60/f5f5f5/a3a3a3",
            "name": "Smart Watch",
            "quantity": 1,
            "price": 199.99
        },
        {
            "image": "https://placehold.co/60x60/f5f5f5/a3a3a3",
            "name": "USB-C Charger",
            "quantity": 3,
            "price": 59.97
        },
        {
            "image": "https://placehold.co/60x60/f5f5f5/a3a3a3",
            "name": "Wireless Mouse",
            "quantity": 1,
            "price": 39.99
        }
    ]

    PriceBreakdown = {
        "subtotal": 747.98,
        "shipping": 15.00,
        "tax": 76.30,
        "total": 839.28
    }

    context = {'PaymentMethod': PaymentMethod, 'OrderSummaryList': OrderSummaryList, 'PriceBreakdown': PriceBreakdown}
    return render(request, 'checkout.html', context)



