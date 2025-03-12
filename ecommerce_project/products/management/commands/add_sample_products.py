from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Add sample products and categories'

    def handle(self, *args, **kwargs):
        # Sample categories with descriptions
        categories_data = [
            {
                'name': 'Laptops & Computers',
                'description': 'High-performance laptops and desktop computers for work and gaming'
            },
            {
                'name': 'Gaming Accessories',
                'description': 'Gaming peripherals, controllers, and accessories'
            },
            {
                'name': 'Audio Equipment',
                'description': 'Headphones, speakers, and audio accessories'
            },
            {
                'name': 'Mobile Phones',
                'description': 'Smartphones and mobile accessories'
            },
            {
                'name': 'Cameras & Photography',
                'description': 'Digital cameras, lenses, and photography equipment'
            },
            {
                'name': 'Smart Home Devices',
                'description': 'Smart speakers, security cameras, and home automation'
            },
            {
                'name': 'Wearable Technology',
                'description': 'Smartwatches, fitness trackers, and wearable devices'
            },
            {
                'name': 'Computer Components',
                'description': 'PC parts, graphics cards, and hardware components'
            },
            {
                'name': 'Networking Equipment',
                'description': 'Routers, switches, and networking accessories'
            },
            {
                'name': 'Office Electronics',
                'description': 'Printers, scanners, and office equipment'
            }
        ]

        # Sample products with Unsplash image URLs
        products_data = {
            'Laptops & Computers': [
                ('Gaming Laptop', 'High-performance gaming laptop with RGB keyboard', 'products/laptop-gaming.jpg', 1299.99),
                ('Business Laptop', 'Slim and lightweight laptop for professionals', 'products/laptop-business.jpg', 999.99),
                ('Desktop PC', 'Custom-built desktop computer for gaming', 'products/desktop-pc.jpg', 1499.99),
                ('Mini PC', 'Compact desktop computer for home office', 'products/mini-pc.jpg', 599.99),
                ('Workstation', 'Professional workstation for content creation', 'products/workstation.jpg', 1999.99),
                ('Chromebook', 'Affordable laptop for web browsing and basic tasks', 'products/chromebook.jpg', 299.99),
                ('All-in-One PC', 'Sleek all-in-one desktop computer', 'products/all-in-one.jpg', 899.99),
                ('Student Laptop', 'Budget-friendly laptop for students', 'products/student-laptop.jpg', 499.99),
                ('Creator Laptop', 'Laptop optimized for creative professionals', 'products/creator-laptop.jpg', 1599.99),
                ('Server PC', 'Small business server computer', 'products/server-pc.jpg', 1299.99)
            ],
            'Gaming Accessories': [
                ('Gaming Mouse', 'High-precision gaming mouse with RGB lighting', 'products/gaming-mouse.jpg', 79.99),
                ('Mechanical Keyboard', 'RGB mechanical gaming keyboard', 'products/mechanical-keyboard.jpg', 129.99),
                ('Gaming Headset', '7.1 surround sound gaming headset', 'products/gaming-headset.jpg', 99.99),
                ('Gaming Monitor', '27" 144Hz gaming monitor', 'products/gaming-monitor.jpg', 299.99),
                ('Gaming Chair', 'Ergonomic gaming chair with lumbar support', 'products/gaming-chair.jpg', 199.99),
                ('Mouse Pad', 'Extended RGB gaming mouse pad', 'products/mouse-pad.jpg', 29.99),
                ('Controller', 'Wireless gaming controller', 'products/controller.jpg', 59.99),
                ('Webcam', 'HD webcam for streaming', 'products/webcam.jpg', 49.99),
                ('Microphone', 'USB condenser microphone', 'products/microphone.jpg', 89.99),
                ('Capture Card', 'Game capture card for streaming', 'products/capture-card.jpg', 159.99)
            ],
            'Audio Equipment': [
                ('Wireless Earbuds', 'True wireless earbuds with noise cancellation', 'products/wireless-earbuds.jpg', 149.99),
                ('Bluetooth Speaker', 'Portable waterproof Bluetooth speaker', 'products/bluetooth-speaker.jpg', 79.99),
                ('Soundbar', 'Home theater soundbar with subwoofer', 'products/soundbar.jpg', 299.99),
                ('Studio Monitors', 'Professional studio monitor speakers', 'products/studio-monitors.jpg', 399.99),
                ('Turntable', 'Vinyl record player with Bluetooth', 'products/turntable.jpg', 199.99),
                ('DAC/Amp', 'Digital-to-analog converter and headphone amp', 'products/dac-amp.jpg', 249.99),
                ('Wireless Headphones', 'Over-ear wireless headphones', 'products/wireless-headphones.jpg', 179.99),
                ('Microphone Set', 'Professional recording microphone kit', 'products/microphone-set.jpg', 299.99),
                ('Audio Interface', 'USB audio interface for recording', 'products/audio-interface.jpg', 159.99),
                ('DJ Controller', 'Digital DJ controller with software', 'products/dj-controller.jpg', 249.99)
            ],
            'Mobile Phones': [
                ('Flagship Smartphone', 'Latest flagship smartphone with 5G', 'products/flagship-phone.jpg', 999.99),
                ('Budget Smartphone', 'Affordable smartphone with great features', 'products/budget-phone.jpg', 299.99),
                ('Phone Case', 'Protective case with card holder', 'products/phone-case.jpg', 29.99),
                ('Screen Protector', 'Tempered glass screen protector', 'products/screen-protector.jpg', 19.99),
                ('Power Bank', 'Fast-charging portable power bank', 'products/power-bank.jpg', 49.99),
                ('Car Mount', 'Wireless charging car phone mount', 'products/car-mount.jpg', 39.99),
                ('Phone Grip', 'Pop-up phone grip and stand', 'products/phone-grip.jpg', 14.99),
                ('Charging Cable', 'Fast charging USB-C cable', 'products/charging-cable.jpg', 19.99),
                ('Wireless Charger', 'Qi wireless charging pad', 'products/wireless-charger.jpg', 29.99),
                ('Phone Lens Kit', 'Camera lens attachments for phones', 'products/phone-lens.jpg', 39.99)
            ],
            'Cameras & Photography': [
                ('DSLR Camera', 'Professional DSLR camera body', 'products/dslr-camera.jpg', 1499.99),
                ('Mirrorless Camera', 'Compact mirrorless camera', 'products/mirrorless-camera.jpg', 999.99),
                ('Camera Lens', 'Versatile zoom lens', 'products/camera-lens.jpg', 599.99),
                ('Camera Bag', 'Weather-resistant camera backpack', 'products/camera-bag.jpg', 99.99),
                ('Tripod', 'Carbon fiber travel tripod', 'products/tripod.jpg', 199.99),
                ('Flash', 'Professional speedlight flash', 'products/flash.jpg', 299.99),
                ('Memory Card', 'High-speed SD memory card', 'products/memory-card.jpg', 49.99),
                ('Filter Set', 'Professional lens filter kit', 'products/filter-set.jpg', 129.99),
                ('Light Box', 'Portable photo studio light box', 'products/light-box.jpg', 79.99),
                ('Camera Strap', 'Comfortable leather camera strap', 'products/camera-strap.jpg', 39.99)
            ],
            'Smart Home Devices': [
                ('Smart Speaker', 'Voice-controlled smart speaker', 'products/smart-speaker.jpg', 99.99),
                ('Security Camera', 'Wireless security camera system', 'products/security-camera.jpg', 199.99),
                ('Smart Thermostat', 'WiFi-enabled smart thermostat', 'products/smart-thermostat.jpg', 249.99),
                ('Smart Doorbell', 'Video doorbell with two-way audio', 'products/smart-doorbell.jpg', 179.99),
                ('Smart Bulbs', 'Color changing smart LED bulbs', 'products/smart-bulbs.jpg', 39.99),
                ('Smart Lock', 'Keyless entry smart door lock', 'products/smart-lock.jpg', 199.99),
                ('Smart Plug', 'WiFi-controlled smart plug', 'products/smart-plug.jpg', 24.99),
                ('Robot Vacuum', 'Smart robot vacuum cleaner', 'products/robot-vacuum.jpg', 299.99),
                ('Smart Display', 'Smart home control display', 'products/smart-display.jpg', 129.99),
                ('Motion Sensor', 'Wireless motion detector', 'products/motion-sensor.jpg', 34.99)
            ],
            'Wearable Technology': [
                ('Smartwatch', 'Feature-rich smartwatch', 'products/smartwatch.jpg', 299.99),
                ('Fitness Tracker', 'Advanced fitness tracking band', 'products/fitness-tracker.jpg', 99.99),
                ('Smart Glasses', 'AR-enabled smart glasses', 'products/smart-glasses.jpg', 499.99),
                ('Smart Ring', 'Health monitoring smart ring', 'products/smart-ring.jpg', 299.99),
                ('Sport Earbuds', 'Wireless sports earbuds', 'products/sport-earbuds.jpg', 149.99),
                ('Smart Clothing', 'Tech-integrated fitness wear', 'products/smart-clothing.jpg', 99.99),
                ('Sleep Tracker', 'Sleep monitoring device', 'products/sleep-tracker.jpg', 199.99),
                ('Smart Jewelry', 'Fashion-forward smart jewelry', 'products/smart-jewelry.jpg', 159.99),
                ('GPS Watch', 'GPS sports watch', 'products/gps-watch.jpg', 249.99),
                ('Health Monitor', 'Portable health monitoring device', 'products/health-monitor.jpg', 199.99)
            ],
            'Computer Components': [
                ('Graphics Card', 'High-end gaming graphics card', 'products/graphics-card.jpg', 699.99),
                ('Processor', 'Latest generation CPU', 'products/processor.jpg', 399.99),
                ('Motherboard', 'Gaming motherboard', 'products/motherboard.jpg', 299.99),
                ('RAM Kit', '32GB DDR4 RAM kit', 'products/ram-kit.jpg', 199.99),
                ('SSD Drive', '1TB NVMe SSD', 'products/ssd-drive.jpg', 149.99),
                ('Power Supply', 'Modular power supply unit', 'products/power-supply.jpg', 129.99),
                ('CPU Cooler', 'Liquid CPU cooler', 'products/cpu-cooler.jpg', 159.99),
                ('PC Case', 'Mid-tower PC case', 'products/pc-case.jpg', 99.99),
                ('Case Fans', 'RGB case fans pack', 'products/case-fans.jpg', 49.99),
                ('Thermal Paste', 'High-performance thermal paste', 'products/thermal-paste.jpg', 9.99)
            ],
            'Networking Equipment': [
                ('WiFi Router', 'Mesh WiFi system', 'products/wifi-router.jpg', 299.99),
                ('Network Switch', 'Managed network switch', 'products/network-switch.jpg', 199.99),
                ('WiFi Extender', 'WiFi range extender', 'products/wifi-extender.jpg', 79.99),
                ('Network Cable', 'Cat 6 ethernet cable', 'products/network-cable.jpg', 19.99),
                ('NAS Drive', 'Network attached storage', 'products/nas-drive.jpg', 399.99),
                ('Modem', 'Cable modem', 'products/modem.jpg', 149.99),
                ('Network Card', 'WiFi 6 network card', 'products/network-card.jpg', 59.99),
                ('Patch Panel', '24-port patch panel', 'products/patch-panel.jpg', 49.99),
                ('Network Tester', 'Network cable tester', 'products/network-tester.jpg', 29.99),
                ('Firewall', 'Hardware firewall', 'products/firewall.jpg', 299.99)
            ],
            'Office Electronics': [
                ('Laser Printer', 'Color laser printer', 'products/laser-printer.jpg', 399.99),
                ('Document Scanner', 'High-speed document scanner', 'products/document-scanner.jpg', 299.99),
                ('Label Maker', 'Professional label printer', 'products/label-maker.jpg', 79.99),
                ('Paper Shredder', 'Cross-cut paper shredder', 'products/paper-shredder.jpg', 129.99),
                ('Projector', 'HD business projector', 'products/projector.jpg', 599.99),
                ('Calculator', 'Financial calculator', 'products/calculator.jpg', 49.99),
                ('Laminator', 'Document laminator', 'products/laminator.jpg', 89.99),
                ('Voice Recorder', 'Digital voice recorder', 'products/voice-recorder.jpg', 99.99),
                ('Binding Machine', 'Spiral binding machine', 'products/binding-machine.jpg', 149.99),
                ('ID Card Printer', 'ID card printer and scanner', 'products/id-printer.jpg', 499.99)
            ]
        }

        # Create categories
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'slug': slugify(cat_data['name'])
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
            
            # Add products for this category
            if cat_data['name'] in products_data:
                for prod_data in products_data[cat_data['name']]:
                    name, description, image, price = prod_data
                    product, prod_created = Product.objects.get_or_create(
                        name=name,
                        category=category,
                        defaults={
                            'description': description,
                            'slug': slugify(name),
                            'price': Decimal(str(price)),
                            'image': image,
                            'stock': random.randint(10, 100),
                            'available': True
                        }
                    )
                    
                    if prod_created:
                        self.stdout.write(
                            self.style.SUCCESS(f'Created product: {product.name} in {category.name}')
                        )

        self.stdout.write(self.style.SUCCESS('Successfully added sample products and categories')) 