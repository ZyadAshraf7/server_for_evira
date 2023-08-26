from flask import *
import json, time

app = Flask(__name__)

@app.route("/products/clothes",methods=['GET'])
def request_clothes():
    clothes_dataset=[
    {
        "id": 50,
        "title": "AUTOMET Womens Oversized Hoodies Fleece Sweatshirts",
        "price": 26.95,
        "description": "Oversized hoodies, drop shoulder collar, slight stretch,solid color, long sleeve sweater, fall outfits for women, fashion and casual style",
        "category": "clothes",
        "image": "https://m.media-amazon.com/images/I/61wPHp6jvaL._AC_UY550_.jpg",
        "rating": {
            "rate": 4.3,
            "count": 120
        }
    },
    {
        "id": 51,
        "title": "Essentials Men's Tech Stretch Long-Sleeve T-Shirt",
        "price": 15.25,
        "description": "TECH STRETCH FABRIC: An ultra-light weight and breathable fabric, with a soft smooth sheen finish",
        "category": "clothes",
        "image": "https://m.media-amazon.com/images/I/91VXOOO0SkL._AC_UX342_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 32
        }
    },
    {
        "id": 52,
        "title": "ZMPSIISA Women Pants High Waisted Cargo Pants Combat",
        "price": 40.99,
        "description": "made of high-quality long staple cotton fabric and soft elastic wear-resistant fabric, providing high stretch",
        "category": "clothes",
        "image": "https://m.media-amazon.com/images/I/81Dsg+bwqUL._AC_UY445_.jpg",
        "rating": {
            "rate": 4.8,
            "count": 10
        }
    },
        {
            "id": 53,
            "title": "ANRABESS Womens Oversized Sweatshirts Turtleneck Pullover",
            "price": 27.95,
            "description": " Our pullover is made of a cotton blend and features a lightweight fleece-lined fabric that's soft, comfortable, and breathable. Perfect to keep you warm in cold weather.",
            "category": "clothes",
            "image": "https://m.media-amazon.com/images/I/614iu02-TEL._AC_UY445_.jpg",
            "rating": {
                "rate": 4.8,
                "count": 32
            }
        },
        {
            "id": 54,
            "title": "AKEWEI Women Half Zip Sweatshirts Lightweight Quilted",
            "price": 29.25,
            "description": "The zip sweatshirt have chic stand collar can keep neck warmth.Quarter zip design and quilted material complete soft and cozy feel.",
            "category": "clothes",
            "image": "https://m.media-amazon.com/images/I/719ZQRPW6YL._AC_UX342_.jpg",
            "rating": {
                "rate": 4.8,
                "count": 12
            }
        },
        {
            "id": 55,
            "title": "J.VER Men's Cotton Linen Short Sleeve Shirts Casual Lightweight",
            "price": 25.99,
            "description": "The casual short sleeve shirt is made of high-quality cotton and linen fabric with anti-shrink treatment, soft and comfortable",
            "category": "clothes",
            "image": "https://m.media-amazon.com/images/I/7104SjbR1WL._AC_UX342_.jpg",
            "rating": {
                "rate": 4.4,
                "count": 10
            }
        }
]

    json_dump = json.dumps(clothes_dataset)
    return json_dump


@app.route("/products/shoes",methods=['GET'])
def request_shoes():
    shoes_dataset=[
    {
        "id": 56,
        "title": "Amazon Essentials Women's Pointed-Toe",
        "price": 19.92,
        "description": "Classic and versatile flat designed for daily wear and superior fit with casual silhouette with pointed toe shape and flattering profile",
        "category": "shoes",
        "image": "https://m.media-amazon.com/images/I/51PhY+z1hrL._AC_UX395_.jpg",
        "rating": {
            "rate": 4.2,
            "count": 8
        }
    },
    {
        "id": 57,
        "title": "adidas Men's Lite Racer Adapt 5.0 Running Shoe",
        "price": 58.86,
        "description": "MADE WITH RECYCLED CONTENT: Made with a series of recycled materials, this upper features at least 50% recycled content.",
        "category": "shoes",
        "image": "https://m.media-amazon.com/images/I/71EQ1QdcPFL._AC_UX395_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 10
        }
    },
    {
        "id": 58,
        "title": "Under Armour Men's Charged Assert 10 Running Shoe",
        "price": 60.35,
        "description": "Lightweight mesh upper with textured overlay details delivers complete breathability",
        "category": "shoes",
        "image": "https://m.media-amazon.com/images/I/51UjVsCF+fL._AC_UY395_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 13
        }
    },
        {
            "id": 59,
            "title": "TSIODFO Men Sneakers Mesh Breathable Comfort Athletic Sport Running",
            "price": 39.95,
            "description": "Occasion: casual, walking, running,driving , training, indoor, sports, outdoor, travel, workout and so on.",
            "category": "shoes",
            "image": "https://m.media-amazon.com/images/I/81F3tlLqKpL._AC_UY395_.jpg",
            "rating": {
                "rate": 4.1,
                "count": 21
            }
        },
        {
            "id": 60,
            "title": "Chopben Men's Running Shoes Blade",
            "price": 29.25,
            "description": "Ventilating shoes insole which thick to keep a dry, healthy and comfort foot environment.After you walk through the day's work with these shoes, you can keep the shoes dry and comfortable.",
            "category": "shoes",
            "image": "https://m.media-amazon.com/images/I/71pVAQ8PBUL._AC_UY395_.jpg",
            "rating": {
                "rate": 4.2,
                "count": 6
            }
        },
        {
            "id": 61,
            "title": "adidas Men's Daily 3.0 Skate Shoe",
            "price": 59.99,
            "description": "CUSHIONED COMFORT: Enjoy the comfort and performance of OrthoLite sockliner; Officially licensed OrthoLite product",
            "category": "shoes",
            "image": "https://m.media-amazon.com/images/I/71apbZy7jML._AC_SX395._SX._UX._SY._UY_.jpg",
            "rating": {
                "rate": 4.7,
                "count": 23
            }
        }
]

    json_dump = json.dumps(shoes_dataset)
    return json_dump

@app.route("/products/bags",methods=['GET'])
def request_bags():
    bags_dataset=[
    {
        "id": 62,
        "title": "adidas Women's All Me Tote Bag",
        "price": 30.10,
        "description": "2 ways to wear: over your shoulder, or across your body. Premium airmesh material. Premium jacquard 3 stripe webbing detail.",
        "category": "bags",
        "image": "https://m.media-amazon.com/images/I/71QgwS4hCKS._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 23
        }
    },
    {
        "id": 63,
        "title": "Gym Bags for Men Women",
        "price": 19.99,
        "description": "Multi-function Duffle Bag - The padded carrying handle meets the needs of portable use",
        "category": "bags",
        "image": "https://m.media-amazon.com/images/I/810nZZmtB9L._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 12
        }
    },
    {
        "id": 64,
        "title": "BAGSMART Duffle Bag for Travel Duffel Bags",
        "price": 22.08,
        "description": "Large Capacity & Lightweight: Carry on bag 38L capacity can fit in 2-4 days short trip of daily essentials",
        "category": "bags",
        "image": "https://m.media-amazon.com/images/I/71vNQ9BISoL._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.6,
            "count": 34
        }
    },
        {
            "id": 65,
            "title": "Travel Duffel Bag, Sports Tote Gym Bag",
            "price": 23.95,
            "description": "The high density water resistant material can help you to separate dry items and wet items",
            "category": "bags",
            "image": "https://m.media-amazon.com/images/I/715M9AlL9jL._AC_UX385_.jpg",
            "rating": {
                "rate": 4.7,
                "count": 4
            }
        },
        {
            "id": 66,
            "title": "SHRRADOO Anti Theft Laptop Backpack",
            "price": 22.39,
            "description": "LOTS OF STORAGE SPACE&POCKETS: One separate laptop compartment hold 17 Inch Laptop as well as 15.6 Inch.",
            "category": "bags",
            "image": "https://m.media-amazon.com/images/I/71qpXciYP1L._AC_SL1200_.jpg",
            "rating": {
                "rate": 4.7,
                "count": 17
            }
        },
        {
            "id": 67,
            "title": "Travel Laptop Backpack",
            "price": 23.99,
            "description": "LARGE CAPACITY&MANY POCKETS-This men backpack owns more than 15 independent pockets.",
            "category": "bags",
            "image": "https://m.media-amazon.com/images/I/81GsZBSHZUL._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.7,
                "count": 12
            }
        }
]

    json_dump = json.dumps(bags_dataset)
    return json_dump


@app.route("/products/electronics",methods=['GET'])
def request_electronics():
    electronics_dataset=[
    {
        "id": 68,
        "title": "LORYERGO Laptop Stand",
        "price": 19.99,
        "description": "Fits 10”-15.6” Laptops - This universal laptop stand works with all laptops with a size within 10-15.6 inches. It is compatible with MacBook, MacBook Pro/ Air, Asus, Sony, Dell, HP,",
        "category": "electronics",
        "image": "https://m.media-amazon.com/images/I/61srHVHN2GL._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 56
        }
    },
    {
        "id": 69,
        "title": "Crucial X9 Pro 2TB Portable SSD",
        "price": 109.99,
        "description": "Powerful performance: With read and write speeds up to 1,050MB/s, the Crucial X9 Pro Portable SSD is powerful enough for editing directly from the drive",
        "category": "electronics",
        "image": "https://m.media-amazon.com/images/I/618815Pud-L._AC_SL1080_.jpg",
        "rating": {
            "rate": 4.9,
            "count": 9
        }
    },
    {
        "id": 70,
        "title": "Leather Desk Pad Protector",
        "price": 13.99,
        "description": "PROTECT YOUR DESK:Made of durable PU leather material, which protects your desk from scratches, stains, spills, heat and scuffs.",
        "category": "electronics",
        "image": "https://m.media-amazon.com/images/I/71miLdyaA7L._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 56
        }
    },
        {
            "id": 71,
            "title": "USB Port Expander USB 3.0 Hub Multiple USB Port USB",
            "price": 11.95,
            "description": "【High-speed and secure data transfer】This USB Splitter can complete data transfer safely and quickly, when using the USB3.0 interface",
            "category": "electronics",
            "image": "https://m.media-amazon.com/images/I/61TF+4d5l8L._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.7,
                "count": 45
            }
        },
        {
            "id": 72,
            "title": "Toshiba Canvio Basics 2TB Portable External Hard Drive",
            "price": 58.39,
            "description": "Sleek profile design with a matte, smudge-resistance finish. Quickly add more storage capacity to your PC and other compatible devices",
            "category": "electronics",
            "image": "https://m.media-amazon.com/images/I/91e-WNUpH0L._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.3,
                "count": 12
            }
        },
        {
            "id": 73,
            "title": "Lucktiger 1TB USB Flash Drive",
            "price": 25.99,
            "description": "PORTABLE AND LIGHTWEIGHT 】- Lucktiger Thumb Drive weigh only 10g. Instant storage for your laptops, tablets, TV’s, and more",
            "category": "electronics",
            "image": "https://m.media-amazon.com/images/I/51ndvZ9G5xL._AC_SL1451_.jpg",
            "rating": {
                "rate": 4.2,
                "count": 23
            }
        }
]

    json_dump = json.dumps(electronics_dataset)
    return json_dump

@app.route("/products/watches",methods=['GET'])
def request_watches():
    watches_dataset=[
    {
        "id": 74,
        "title": "BY BENYAR Men's Watches Waterproof",
        "price": 39.99,
        "description": "Branded tactical watch Movement make it accuracy rate less than 1 second per day, it will always tell you accurate time in occasion, business, or other important places.",
        "category": "watches",
        "image": "https://m.media-amazon.com/images/I/71kzslUzjHL._AC_UX466_.jpg",
        "rating": {
            "rate": 4.4,
            "count": 34
        }
    },
    {
        "id": 75,
        "title": "BEN NEVIS Mens Watches",
        "price": 26.99,
        "description": "[Ultra-thin Simple Design]: Ultra-thin 6.7 mm thickness dial with rounded black lines watch case, minimalist style appearance, unique and eye-catching.",
        "category": "watches",
        "image": "https://m.media-amazon.com/images/I/61QeNWSSHaL._AC_UX466_.jpg",
        "rating": {
            "rate": 4.2,
            "count": 56
        }
    },
    {
        "id": 76,
        "title": "MEGIR Men's Business Analog Chronograph",
        "price": 35.99,
        "description": "Fashion Watch for Men: Quartz movement, accurate time keeping. Hardlex wear-resistant crystal and leather band with a safety clasp.",
        "category": "watches",
        "image": "https://m.media-amazon.com/images/I/61MklczvgIL._AC_UX466_.jpg",
        "rating": {
            "rate": 4.2,
            "count": 34
        }
    },
        {
            "id": 77,
            "title": "MEGIR Men's Analog Business Quartz",
            "price": 35.95,
            "description": "Business Watches for Men -- Quartz movement, accurate time keeping. 3 sub-dials, analog display, Hardlex dial window, clear dial, alloy case, comfortable adjustable wristband",
            "category": "watches",
            "image": "https://m.media-amazon.com/images/I/61oRTQHKR7L._AC_UX466_.jpg",
            "rating": {
                "rate": 4.3,
                "count": 57
            }
        },
        {
            "id": 78,
            "title": "OLEVS Watch for Men Stylish Black Silicone",
            "price": 58.39,
            "description": "Fashion Sports Watches For Men:The stylish and individual analog quartz mens watch adopts a new visual design, and the luxury big dial is matched with 8 bright diamonds",
            "category": "watches",
            "image": "https://m.media-amazon.com/images/I/61ErXu46krL._AC_UX466_.jpg",
            "rating": {
                "rate": 4.3,
                "count": 78
            }
        },
        {
            "id": 79,
            "title": "OLEVS Automatic Watches for Men Diamond Skeleton",
            "price": 138.99,
            "description": "Men's automatic watch: Imported automatic movement, traditional exquisite craftsmanship, can operate stably for more than 10 years.",
            "category": "watches",
            "image": "https://m.media-amazon.com/images/I/71gNZL7tygL._AC_UY500_.jpg",
            "rating": {
                "rate": 4.9,
                "count": 125
            }
        }
]

    json_dump = json.dumps(watches_dataset)
    return json_dump


@app.route("/products/jewelry",methods=['GET'])
def request_jewelry():
    jewelry_dataset=[
    {
        "id": 80,
        "title": "Birthstone Necklace Love Gifts for Women, 925 Sterling Silver",
        "price": 59.99,
        "description": "UNIQUE NECKLACE DESIGN The unique Love knot and the design of heart birthstone symbolize your eternal love",
        "category": "jewelry",
        "image": "https://m.media-amazon.com/images/I/61PLMYXKlnL._AC_UX385_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 76
        }
    },
    {
        "id": 81,
        "title": "Leafael Necklaces for Women",
        "price": 31.99,
        "description": "Heart Necklaces with Birthstone Crystals - Our Infinity Love heart necklace for women is an original design from our studio in Boston",
        "category": "jewelry",
        "image": "https://m.media-amazon.com/images/I/71e+M9NJw-L._AC_UX342_.jpg",
        "rating": {
            "rate": 4.6,
            "count": 56
        }
    },
    {
        "id": 82,
        "title": "S925 Sterling Silver Necklace for Women",
        "price": 103.99,
        "description": "【Necklace Jewelry that is S925 Sterling Silver All Over】Everything is S925 sterling silver including the chain",
        "category": "jewelry",
        "image": "https://m.media-amazon.com/images/I/719RoxeMg-L._AC_UX342_.jpg",
        "rating": {
            "rate": 4.1,
            "count": 65
        }
    },
        {
            "id": 83,
            "title": "Leafael Infinity Love Heart Link Bracelets",
            "price": 39.95,
            "description": "Elegant Charm Bracelets - Our aesthetic bracelets for women are designed in Boston and feature precious Austrian crystals",
            "category": "jewelry",
            "image": "https://m.media-amazon.com/images/I/71FI5cRBvxL._AC_UX385_.jpg",
            "rating": {
                "rate": 4.4,
                "count": 53
            }
        },
        {
            "id": 84,
            "title": "PAVOI 14K Gold Plated 3mm Cubic Zirconia",
            "price": 35.39,
            "description": "bracelet featuring round 3mm AAAAA cubic zirconia stones in four-prong basket settings. Measures 6.5 inches in Length",
            "category": "jewelry",
            "image": "https://m.media-amazon.com/images/I/610VsCaFMXL._AC_UX385_.jpg",
            "rating": {
                "rate": 4.6,
                "count": 45
            }
        },
        {
            "id": 85,
            "title": "SmileBelle Tennis Bracelets for Women",
            "price": 12.99,
            "description": "High-Quality Materials: We prioritize your comfort and safety, which is why our bracelets tennis is lead-free.",
            "category": "jewelry",
            "image": "https://m.media-amazon.com/images/I/61QWNkNSECL._AC_UX385_.jpg",
            "rating": {
                "rate": 4.9,
                "count": 125
            }
        }
]

    json_dump = json.dumps(jewelry_dataset)
    return json_dump


@app.route("/products/kitchen",methods=['GET'])
def request_kitchen():
    kitchen_dataset=[
    {
        "id": 86,
        "title": "Mixing Bowls with Airtight Lids Set, 26PCS Stainless Steel",
        "price": 42.99,
        "description": "AIRTIGHT LIDS & 3 GRATER ATTACHMENTS The airtight lids that come with this mixing bowl set make it easy to store ingredients and leftovers without worrying about spills or leaks.",
        "category": "kitchen",
        "image": "https://m.media-amazon.com/images/I/71CS445b7eL._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 76
        }
    },
    {
        "id": 87,
        "title": "Mixing Bowls with Airtight Lids, 20PCS Stainless Steel",
        "price": 39.99,
        "description": "ROTTAY versatile combination set includes 6 size mixing bowls - 7, 4, 3, 2, 1.5, 1 QT. The lid of the 4 QT bowl has a removable center, where can be placed one of 3 free graters to grate something",
        "category": "kitchen",
        "image": "https://m.media-amazon.com/images/I/615auzqIQtS._AC_SL1010_.jpg",
        "rating": {
            "rate": 4.6,
            "count": 56
        }
    },
    {
        "id": 88,
        "title": "ropoda Pickleball Paddles, Lightweight Fiberglass Surface",
        "price": 33.99,
        "description": "Fiberglass surface and honeycomb core internal structure make the pickle ball paddles light and durable for an ideal level of strength and stiffness",
        "category": "kitchen",
        "image": "https://m.media-amazon.com/images/I/91p8CLbIbWL._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.1,
            "count": 65
        }
    },
        {
            "id": 89,
            "title": "McCook® MC21G Knife Sets,15 Pieces",
            "price": 87.95,
            "description": "EXCLUSIVE BUILT-IN SHARPENER – Stainless steel knife block set with built-in sharpener is amazing. It saves you from having to honing blades on a sharpening steel.",
            "category": "kitchen",
            "image": "https://m.media-amazon.com/images/I/81eoRTjyzNL._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.4,
                "count": 53
            }
        },
        {
            "id": 90,
            "title": "WIZEKA Kitchen Knife Set with Block, NSF Certified 15pcs German Steel",
            "price": 139.39,
            "description": "Expertly crafted and forged from 1.4116 high carbon German steel with a hand polished edge at 14 degrees per side",
            "category": "kitchen",
            "image": "https://m.media-amazon.com/images/I/71iFK620R1L._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.6,
                "count": 45
            }
        },
        {
            "id": 91,
            "title": "Skroam 36 Pack Food Storage Containers with lids ",
            "price": 23.99,
            "description": "All Possible Sizes - This 36pcs stackable storage containers set comes 18 containers with 18 lids of multiple sizes",
            "category": "kitchen",
            "image": "https://m.media-amazon.com/images/I/81mYgk0KBEL._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.9,
                "count": 125
            }
        }
]

    json_dump = json.dumps(kitchen_dataset)
    return json_dump

@app.route("/products/toys",methods=['GET'])
def request_toys():
    toys_dataset=[
    {
        "id": 92,
        "title": "McFarlane Toys - DC Multiverse Batman (Dark Knights of Steel)",
        "price": 19.99,
        "description": "Designed with Ultra Articulation with up to 22 moving parts for full range of posing and play. Dark Knights of Steel Batman includes sword and base",
        "category": "toys",
        "image": "https://m.media-amazon.com/images/I/71UXzhyGilL._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 76
        }
    },
    {
        "id": 93,
        "title": "STSGPUZ Kids 𝟑𝟔 𝐢𝐧𝐜𝐡𝐞𝐬. 𝐁𝐨𝐰 𝐚𝐧𝐝 𝐀𝐫𝐫𝐨𝐰",
        "price": 39.99,
        "description": "Aim and shoot immediately - Package includes 36 inches. main bow body, 16 suction cup arrows, target and quiver.",
        "category": "toys",
        "image": "https://m.media-amazon.com/images/I/71iewlmiySL._AC_SL1500_.jpg",
        "rating": {
            "rate": 4.6,
            "count": 56
        }
    },
    {
        "id": 94,
        "title": "Kids Basketball Hoop Adjustable Height 2.9 ft-6.2 ft",
        "price": 35.99,
        "description": "Easy to Install: Kids basketball hoop includes 2*bouncy mini balls, pump, basketball hoops and other accessories.",
        "category": "toys",
        "image": "https://m.media-amazon.com/images/I/51ATKzZzQ9L._AC_SL1000_.jpg",
        "rating": {
            "rate": 4.1,
            "count": 65
        }
    },
        {
            "id": 95,
            "title": "Transformers Toys Studio Series",
            "price": 89.95,
            "description": "THE TRANSFORMERS: THE MOVIE ULTRA MAGNUS: This Transformers Studio Series 86-21 Ultra Magnus action figure.",
            "category": "toys",
            "image": "https://m.media-amazon.com/images/I/71PGbOv72SL._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.4,
                "count": 53
            }
        },
        {
            "id": 96,
            "title": "LEGO Harry Potter Hogwarts Express",
            "price": 119.39,
            "description": "LEGO Harry Potter train set (76423) – Recreate the memorable scene where Hagrid greets first-year Hogwarts students arriving at Hogsmeade Station on the Hogwarts Express",
            "category": "toys",
            "image": "https://m.media-amazon.com/images/I/81k2q9pSo4L._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.6,
                "count": 45
            }
        },
        {
            "id": 97,
            "title": "LEGO Star Wars Ultimate Millennium Falcon",
            "price": 837.99,
            "description": "Ultimate Build - Defend the Galaxy and build the largest LEGO Star Wars Millennium Falcon to date! The perfect set for adult Star Wars fans and expert builders",
            "category": "toys",
            "image": "https://m.media-amazon.com/images/I/91FoS63ClXL._AC_SL1500_.jpg",
            "rating": {
                "rate": 4.9,
                "count": 125
            }
        }
]

    json_dump = json.dumps(toys_dataset)
    return json_dump


if(__name__ == '__main__'):
    app.run(port=7777)