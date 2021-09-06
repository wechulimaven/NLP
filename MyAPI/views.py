from django.shortcuts import render
from django.contrib import messages

from . forms import TextLangForm

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from . models import translator

from django.db.models import Q

from django.views.generic import ListView



url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/1f630c99-7be8-4f3c-a14d-90498f3b9589'
apikey_lt='O45OEmNBnevMrfBb1N2bhNcvrWm8eOY9tlY3ihGh-C11'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)


def translated(request):
	if request.method=="POST":
		form = TextLangForm(request.POST)
		if form.is_valid():
			Text = form.cleaned_data['text']
			Lang1 = form.cleaned_data['lang1']
			Lang2 = form.cleaned_data['lang2']
			if Lang1==Lang2:
				messages.success(request,Text)
			elif Lang1!='en' and Lang2!='en':
				Lang3 = 'en'
				Lang = Lang1+'-'+Lang3
				translation_response = language_translator.translate(text=Text, model_id=Lang)
				translation=translation_response.get_result()
				translation =translation['translations'][0]['translation']
				Lang = Lang3+'-'+Lang2
				translation_response = language_translator.translate(text=translation, model_id=Lang)
				translation=translation_response.get_result()
				translation =translation['translations'][0]['translation']
				messages.success(request,translation)
			else:
				Lang = Lang1+'-'+Lang2
				translation_response = language_translator.translate(text=Text, model_id=Lang)
				translation=translation_response.get_result()
				translation =translation['translations'][0]['translation']
				messages.success(request,translation)

	form = TextLangForm()
	return render(request, 'MyAPI/form.html', {'form':form})

def about(request):
	return render(request, 'MyAPI/about.html')

def index(request):
    #if request.user.is_authenticated():
     #   return render(request, 'music/login.html')
    #else:
    albums = translator.objects.all()
    # song_results = Song.objects.all()
    query = request.GET.get("q")
    if query:
    	albums = albums.filter(
		Q(english__icontains=query) |
		Q(luo__icontains=query)
	).distinct()
        # song_results = song_results.filter(
        #     Q(song_title__icontains=query)
        # ).distinct()
    	return render(request, 'MyAPI/index.html', {
            'albums': albums,
            # 'songs': song_results,
        })
    else:
	    return render(request, 'MyAPI/index.html')


class SearchResultsView(ListView):
    model = translator
    template_name = 'MyAPI/search.html'
    paginate_by = 3
    page_kwarg = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = translator.objects.filter(
            Q(english__icontains=query) | Q(luo__icontains=query)
        )
        return object_list

    # def get_queryset(self): # new
    #     query = self.request.GET.get('q')
    #     object_list = translator.objects.filter(
    #         Q(english__icontains=query) | Q(luo__icontains=query)
    #     )
    #     return object_list