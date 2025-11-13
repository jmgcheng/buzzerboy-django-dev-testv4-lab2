from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from page.forms import ContactForm
# from django.utils.translation import gettext as _
# from django.utils import translation
# from django.conf import settings


def index(request):
    # 
    section_hero = {
        'header': 'Your Project to the Next Level with Kadso Admin Dashboard',
        'description': 'Forge polished admin interfaces effortlessly with our go-to solution. Simplify your workflow and elevate user experience seamlessly.',
    }

    # 
    section_clients = {
        'header': 'Trusted By World Best Companies',
    }
    clients = [
        'assets/images/landing/client/clients-logo-1.svg',
        'assets/images/landing/client/clients-logo-2.svg',
        'assets/images/landing/client/clients-logo-3.svg',
        'assets/images/landing/client/clients-logo-4.svg',
        'assets/images/landing/client/clients-logo-5.svg',
    ]

    # 
    section_services = {
        'name_text': 'Services',
        'header': "Crafting sleek and engaging websites that captivate audiences and elevate brands.",
        'description': "We specialize in crafting fully customizable services tailored precisely to meet your <br> distinct needs, Whether you're aiming to increase brand awareness.",
    }
    services = [
        {
            'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 16 16"><path fill="#4a98f5" d="M16 0s-3.5-.4-6.7 2.8C7.7 4.3 6.4 6.3 5.4 8.1l-2.5-.6l-1.6 1.6l2.8 1.4c-.3.6-.4 1-.4 1l.8.8s.4-.2 1-.4l1.4 2.8l1.6-1.6l-.5-2.5c1.7-1 3.8-2.3 5.3-3.8C16.4 3.6 16 0 16 0m-3.2 4.8c-.4.4-1.1.4-1.6 0c-.4-.4-.4-1.1 0-1.6c.4-.4 1.1-.4 1.6 0c.4.4.4 1.1 0 1.6"/><path fill="#4a98f5" d="M4 14.2c-.8.8-2.6.4-2.6.4s-.4-1.8.4-2.6s1.5-.9 1.5-.9s-1.3-.3-2.1.6c-1.6 1.6-1 4.2-1 4.2s2.6.6 4.2-1c.9-.9.6-2.2.6-2.2s-.2.7-1 1.5"/></svg>',
            'header': 'All-in-one toolkit',
            'description': 'Empower your digital product business with an all-in-one solution packed with innovative tools. From launch to success, access everything you need.',
        },
        {
            'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#4a98f5" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3" opacity="0.5"/><path fill="#4a98f5" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14z"/></svg>',
            'header': 'Business insights',
            'description': 'All the innovative tools you need to launch a lucrative digital product business in one neat little package.',
        },
        {
            'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#4a98f5" fill-rule="evenodd" d="M19 21.5H6A3.5 3.5 0 0 1 2.5 18V4.943c0-1.067 1.056-1.744 1.985-1.422c.133.046.263.113.387.202l.175.125a2.51 2.51 0 0 0 2.912-.005a3.52 3.52 0 0 1 4.082 0a2.51 2.51 0 0 0 2.912.005l.175-.125c.993-.71 2.372 0 2.372 1.22V12.5H21a.75.75 0 0 1 .75.75v5.5A2.75 2.75 0 0 1 19 21.5M17.75 14v4.75a1.25 1.25 0 0 0 2.5 0V14zM13.5 9.75a.75.75 0 0 0-.75-.75h-6a.75.75 0 0 0 0 1.5h6a.75.75 0 0 0 .75-.75m-1 3a.75.75 0 0 0-.75-.75h-5a.75.75 0 1 0 0 1.5h5a.75.75 0 0 0 .75-.75m.25 2.25a.75.75 0 1 1 0 1.5h-6a.75.75 0 0 1 0-1.5z" clip-rule="evenodd"/></svg>',
            'header': 'Invoicing',
            'description': 'Revolutionize your invoicing process with our streamlined solution! Say goodbye to tedious manual invoicing and hello to beautifully.',
        },
        {
            'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#4a98f5" d="M12 2C6.486 2 2 6.486 2 12v4.143C2 17.167 2.897 18 4 18h1a1 1 0 0 0 1-1v-5.143a1 1 0 0 0-1-1h-.908C4.648 6.987 7.978 4 12 4s7.352 2.987 7.908 6.857H19a1 1 0 0 0-1 1V18c0 1.103-.897 2-2 2h-2v-1h-4v3h6c2.206 0 4-1.794 4-4c1.103 0 2-.833 2-1.857V12c0-5.514-4.486-10-10-10"/></svg>',
            'header': 'Awesome Support',
            'description': 'Discover the unparalleled support experience you deserve with our Awesome Support service. Our dedicated team is committed to your success.',
        },
        {
            'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#4a98f5" d="M4 13h6c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v8c0 .55.45 1 1 1m0 8h6c.55 0 1-.45 1-1v-4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v4c0 .55.45 1 1 1m10 0h6c.55 0 1-.45 1-1v-8c0-.55-.45-1-1-1h-6c-.55 0-1 .45-1 1v8c0 .55.45 1 1 1M13 4v4c0 .55.45 1 1 1h6c.55 0 1-.45 1-1V4c0-.55-.45-1-1-1h-6c-.55 0-1 .45-1 1"/></svg>',
            'header': 'Smart Dashboards',
            'description': 'Welcome to the era of intelligent dashboards—your gateway to streamlined data management. Our smart dashboards offer a user-friendly.',
        },
        {
            'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#4a98f5" d="M16.519 16.501c.175-.136.334-.295.651-.612l3.957-3.958c.096-.095.052-.26-.075-.305a4.332 4.332 0 0 1-1.644-1.034a4.332 4.332 0 0 1-1.034-1.644c-.045-.127-.21-.171-.305-.075L14.11 12.83c-.317.317-.476.476-.612.651c-.161.207-.3.43-.412.666c-.095.2-.166.414-.308.84l-.184.55l-.292.875l-.273.82a.584.584 0 0 0 .738.738l.82-.273l.875-.292l.55-.184c.426-.142.64-.212.84-.308c.236-.113.46-.25.666-.412m5.849-5.809a2.163 2.163 0 1 0-3.06-3.059l-.126.128a.524.524 0 0 0-.148.465c.02.107.055.265.12.452c.13.375.376.867.839 1.33a3.5 3.5 0 0 0 1.33.839c.188.065.345.1.452.12a.525.525 0 0 0 .465-.148z"/><path fill="#4a98f5" fill-rule="evenodd" d="M4.172 3.172C3 4.343 3 6.229 3 10v4c0 3.771 0 5.657 1.172 6.828C5.343 22 7.229 22 11 22h2c3.771 0 5.657 0 6.828-1.172C20.981 19.676 21 17.832 21 14.18l-2.818 2.818c-.27.27-.491.491-.74.686a5.107 5.107 0 0 1-.944.583a8.163 8.163 0 0 1-.944.355l-2.312.771a2.083 2.083 0 0 1-2.635-2.635l.274-.82l.475-1.426l.021-.066c.121-.362.22-.658.356-.944c.16-.335.355-.651.583-.943c.195-.25.416-.47.686-.74l4.006-4.007L18.12 6.7l.127-.127A3.651 3.651 0 0 1 20.838 5.5c-.151-1.03-.444-1.763-1.01-2.328C18.657 2 16.771 2 13 2h-2C7.229 2 5.343 2 4.172 3.172M7.25 9A.75.75 0 0 1 8 8.25h6.5a.75.75 0 0 1 0 1.5H8A.75.75 0 0 1 7.25 9m0 4a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5H8a.75.75 0 0 1-.75-.75m0 4a.75.75 0 0 1 .75-.75h1.5a.75.75 0 0 1 0 1.5H8a.75.75 0 0 1-.75-.75" clip-rule="evenodd"/></svg>',
            'header': 'Well Documented',
            'description': 'Explore our meticulously crafted digital product solution, meticulously documented for your ease. Dive into a wealth of comprehensive.',
        },
    ]    

    # 
    section_features = {
        'name_text': 'Feature',
        'header': "Our key feature",
        'description': 'Our features that Streamlining Healthcare Management.',
    }
    features = [
        'Accurate information',
        'Appointment Management',
        'Revenue Optimization', 
        'Inter-Team Collaboration', 
        'Interface customization', 
        'Improved Patient Care'
    ]

    # 
    section_testimonials = {
        'name_text': 'Testimonials',
        'header': "Our Platform's Impact In <br> Their Own Words",
        'description': 'Dive into inspiring success stories that showcase how <br> our platform has empowered admin dashboard.',
    }
    testimonials = [
        {
            'content': 'Without a doubt, Spend in stands out as the absolute best.Their exceptional quality, reliablity, and customer service are unmatched. I have complete....',
            'name': 'Moritika Kazuki',
            'from': 'Finance Manager at Mangan',
            'image': 'user-4.jpg',
        }, 
        {
            'content': 'I am extremely delighated with the exceptional service provided by NioLand. Their expert support system, efficient tools, and strategic solutions have truly....',
            'name': 'Jimmy Bartney',
            'from': 'Product Manager At Picko Lab',
            'image': 'user-2.jpg',
        }, 
        {
            'content': 'As a satisfied user, I can confidence say that my experience with NioLand has been outstanding. The service, support, and solutions provided have...',
            'name': 'Natasha Romanoff',
            'from': 'Black Widow',
            'image': 'user-3.jpg',
        }, 
        {
            'content': "I've tried many services, but none compare to the excellence provided here! From start to finish, the team has been attentive, professional.",
            'name': 'Barbara McIntosh',
            'from': 'Senior Software Developer',
            'image': 'user-6.jpg',
        }, 
    ]

    # 
    section_qas = {
        'name_text': 'Questions & Answer',
        'header': 'Learn more about our platform <br> by user questions',
        'description': 'Dive into inspiring success stories that showcase how <br> our platform has empowered admin dashboard.',
    }
    qas = {'col_1': [{'icon': 'smile', 'title': 'Is there a free trail available?', 'content': 'The admin panel SaaS is a platform that provides administrators with a centralized interface to manage various aspects of their software.'}, {'icon': 'copy', 'title': 'What features does the admin panel SaaS offer?', 'content': 'The features may vary depending on the specific platform, but commonly included features are user authentication and authorization.'}, {'icon': 'disc', 'title': 'How can I sign up for the admin panel SaaS?', 'content': "To sign up, visit our website and follow the registration process. You'll need to provide some basic information and choose a subscription plan."}, {'icon': 'user', 'title': 'What is the Installation?', 'content': 'The Installation SaaS is a platform designed to streamline the installation process for various software applications or systems.'}], 'col_2': [{'icon': 'hard-drive', 'title': 'Is the admin panel customizable?', 'content': 'Yes, the admin panel SaaS often offers customization options to tailor the interface to your specific requirements. This may include branding customization.'}, {'icon': 'loader', 'title': 'Is there a mobile app for the admin panel?', 'content': 'Some admin panel SaaS platforms offer mobile apps or have responsive web designs, allowing you to access the admin panel from mobile devices.'}, {'icon': 'message-square', 'title': 'Can I integrate the admin panel SaaS with other tools or services?', 'content': 'Yes, the admin panel SaaS often supports integrations with various third-party tools and services through APIs or pre-built connectors.'}, {'icon': 'zap', 'title': 'How does it work?', 'content': 'The Buying Product SaaS is a platform that facilitates the purchase process for both buyers and sellers. It provides a centralized marketplace.'}]}

    # 
    section_price = {
        'name_text': 'Pricing plans',
        'header': 'Explore Our Pricing </br> Plan Solutions',
        'description': 'Discover pricing options designed to accommodate </br> pratices of all sizes.',
    }
    price_plans = [
        {
            'title': 'Freelancer',
            'description': 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.',
            'currency': '$',
            'price': '24',
            'per': 'month',
            'features': [
                '5 products',
                'Up to 1,000 subscribers',
                'Basic analytics',
                '48-hour support response time',
            ]
        },
        {
            'title': 'Startup',
            'description': 'Perfect for small teams and growing businesses.',
            'currency': '$',
            'price': '49',
            'per': 'month',
            'features': [
                '20 products',
                'Up to 5,000 subscribers',
                'Advanced analytics',
                '24-hour support response time',
            ]
        },
        {
            'title': 'Enterprise',
            'description': 'Tailored for large organizations with custom needs.',
            'currency': '$',
            'price': '99',
            'per': 'month',
            'features': [
                'Unlimited products',
                'Unlimited subscribers',
                'Full analytics suite',
                'Dedicated support team',
            ]
        },
    ]

    # 
    contact_form = ContactForm()

    data = {
        'page_title': 'Homepage',
        'menu_active': 'homepage',
        'section_hero': section_hero,
        'section_clients': section_clients,
        'clients': clients,
        'section_services': section_services,
        'services': services,
        'section_features': section_features,
        'features': features,
        'section_testimonials': section_testimonials,
        'testimonials': testimonials,
        'section_qas': section_qas,
        'qas': qas,
        'price_plans': price_plans,
        'section_price': section_price,
        'contact_form': contact_form
    }
    return render(request, 'page/homepage.html', data)

@login_required
def pricing(request):

    # 
    section_price = {
        'header': 'Pricing Plans',
        'description': 'We have plans and prices that fit your business perfectly. Make your <br> client site a success with our products.',
    }
    price_plans = [
        {
            'title': 'Freelancer',
            'description': 'Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.',
            'currency': '$',
            'price': '24',
            'per': 'month',
            'features': [
                '5 products',
                'Up to 1,000 subscribers',
                'Basic analytics',
                '48-hour support response time',
            ]
        },
        {
            'title': 'Startup',
            'description': 'Perfect for small teams and growing businesses.',
            'currency': '$',
            'price': '49',
            'per': 'month',
            'features': [
                '20 products',
                'Up to 5,000 subscribers',
                'Advanced analytics',
                '24-hour support response time',
            ]
        },
        {
            'title': 'Enterprise',
            'description': 'Tailored for large organizations with custom needs.',
            'currency': '$',
            'price': '99',
            'per': 'month',
            'features': [
                'Unlimited products',
                'Unlimited subscribers',
                'Full analytics suite',
                'Dedicated support team',
            ]
        },
    ]

    data = {
        'page_title': 'Pricing',
        'menu_active': 'pricing',

        'section_price': section_price,        
        'price_plans': price_plans,
    }
    return render(request, 'page/pricing.html', data)


@login_required
def dashboard(request):
    data = {
        'page_title': 'Dashboard',
        'menu_active': 'dashboard',
    }
    return render(request, 'page/dashboard.html', data)
