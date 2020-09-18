from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactsView(TemplateView):
    template_name = 'contact.html'


class FeedBackView(TemplateView):
    template_name = 'feedback.html'
