# from django.conf import settings


# class LanguageCookieMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)

#         lang = getattr(request, "_preferred_lang_cookie", None)
#         if lang:
#             response.set_cookie(
#                 settings.LANGUAGE_COOKIE_NAME,
#                 lang,
#                 path=settings.LANGUAGE_COOKIE_PATH,
#                 domain=settings.LANGUAGE_COOKIE_DOMAIN,
#                 secure=settings.LANGUAGE_COOKIE_SECURE,
#                 httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
#                 samesite=settings.LANGUAGE_COOKIE_SAMESITE,
#             )
#         return response
