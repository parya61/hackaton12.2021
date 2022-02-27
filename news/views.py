from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import TemplateView
from .forms import UploadFileForm
import re
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    PER,
    NamesExtractor,
    Doc
)


def text(request):
    context={

    }
    if request.method == 'POST':

        buton = request.POST.get('action')
        name = request.POST['name']

        q = name



        bulkemails = q


        segmenter = Segmenter()
        morph_vocab = MorphVocab()
        emb = NewsEmbedding()
        morph_tagger = NewsMorphTagger(emb)
        syntax_parser = NewsSyntaxParser(emb)
        ner_tagger = NewsNERTagger(emb)
        names_extractor = NamesExtractor(morph_vocab)

        doc = Doc(bulkemails)
        doc.segment(segmenter)

        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)
        doc.tag_ner(ner_tagger)
        for token in doc.tokens:
            token.lemmatize(morph_vocab)
        for span in doc.spans:
            span.normalize(morph_vocab)
        fio = ''
        for span in doc.spans:
            if span.type == PER:
                span.extract_fact(names_extractor)
        names_dict = {_.normal: _.fact.as_dict for _ in doc.spans if _.fact}
        for key in names_dict:
            fio +=(key)


        r = re.compile('')
        t = re.sub(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)','x',bulkemails)
        t = re.sub(r'(\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b)','x',t)
        t = re.sub(r'(\d{4}[\s\-]*\d{4}[\s\-]*\d{4}[\s\-]*\d{4})','x',t)
        #дата
        t = re.sub(r'(\d{2}.\d{2}.\d{4}\s\года\s\рождения)','x',t)
        t = re.sub(r'(родившийся\s\d{2}.\d{2}.\d{4}\s\года)','x',t)
        t = re.sub(r'(дата\s\рождения\s\d{2}.\d{2}.\d{4})','x',t)
        # t = re.sub(r'(\d{2}-\d{2}-\d{4})','x'+cr,t)
        #серия паспорта
        t = re.sub(r'(\b\w{5}\b\s\d{4}\b)','x',t)
        #номер паспорта
        t = re.sub(r'(\b\w{5}\b\s\d{6}\b)','x',t)
        #адресу
        t = re.sub(r'(улица\s\w+\b)','x',t)
        t = re.sub(r'(ул.\s\w+\b)','x',t)
        t = re.sub(r'(дом\s\d+\b)','x',t)
        t = re.sub(r'(д.\s\d+\b)','x',t)
        #фио
        t = re.sub(r'([А-Я][а-я]+\s+[А-Я]\.[А-Я]\.)','x',t)
        t = re.sub(r'([А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+\s)','x',t)
        t = re.sub(r'([А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+[,])','x',t)


        results = r.findall(bulkemails)
        emails = ""
        for x in results:
                emails += str(x)+"\n"


        context = {
            'hop':t,
            'name':name,
        }



        if buton == 'Сохранить в БД':
            st = request.POST.get('name')
            fin = request.POST.get('hop')
            obj = Articles()
            obj.start = st
            obj.finish = fin
            obj.save()

    return render(request, 'news/news_home.html',context)

def file(request):
    context={
        'a':' '
    }

    if request.method == 'POST':
        uploaded_file = request.FILES['doc'].read().decode('utf8')

        button = request.POST.get('button')
        buton = request.POST.get('action')


        context={
            'uploaded_file':uploaded_file
        }

        if (button == 'Загрузить файл и сохранить в БД') :



            print(uploaded_file)
            buttton = request.POST.get('button')


            context={
                'uploaded_file':uploaded_file
            }
            bulkemails = uploaded_file


            segmenter = Segmenter()
            morph_vocab = MorphVocab()
            emb = NewsEmbedding()
            morph_tagger = NewsMorphTagger(emb)
            syntax_parser = NewsSyntaxParser(emb)
            ner_tagger = NewsNERTagger(emb)
            names_extractor = NamesExtractor(morph_vocab)

            doc = Doc(bulkemails)
            doc.segment(segmenter)

            doc.tag_morph(morph_tagger)
            doc.parse_syntax(syntax_parser)
            doc.tag_ner(ner_tagger)
            for token in doc.tokens:
                token.lemmatize(morph_vocab)
            for span in doc.spans:
                span.normalize(morph_vocab)
            fio = ''
            for span in doc.spans:
                if span.type == PER:
                    span.extract_fact(names_extractor)
            names_dict = {_.normal: _.fact.as_dict for _ in doc.spans if _.fact}
            for key in names_dict:
                fio +=(key)


            r = re.compile('')
            t = re.sub(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)','x',bulkemails)
            t = re.sub(r'(\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b)','x',t)
            t = re.sub(r'(\d{4}[\s\-]*\d{4}[\s\-]*\d{4}[\s\-]*\d{4})','x',t)
            #дата
            t = re.sub(r'(\d{2}.\d{2}.\d{4}\s\года\s\рождения)','x',t)
            t = re.sub(r'(родившийся\s\d{2}.\d{2}.\d{4}\s\года)','x',t)
            t = re.sub(r'(дата\s\рождения\s\d{2}.\d{2}.\d{4})','x',t)
            # t = re.sub(r'(\d{2}-\d{2}-\d{4})','x'+cr,t)
            #серия паспорта
            t = re.sub(r'(\b\w{5}\b\s\d{4}\b)','x',t)
            #номер паспорта
            t = re.sub(r'(\b\w{5}\b\s\d{6}\b)','x',t)
            #адресу
            t = re.sub(r'(улица\s\w+\b)','x',t)
            t = re.sub(r'(ул.\s\w+\b)','x',t)
            t = re.sub(r'(дом\s\d+\b)','x',t)
            t = re.sub(r'(д.\s\d+\b)','x',t)
            #фио
            t = re.sub(r'([А-Я][а-я]+\s+[А-Я]\.[А-Я]\.)','x',t)
            t = re.sub(r'([А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+\s)','x',t)
            t = re.sub(r'([А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+[,])','x',t)


            results = r.findall(bulkemails)
            emails = ""
            for x in results:
                    emails += str(x)+"\n"
            context={
                'hop':t,
                'uploaded_file':uploaded_file
            }
            st = uploaded_file
            fin = t
            obj = Articles()
            obj.start = st
            obj.finish = fin
            obj.save()
            print(context)
            return render(request, 'news/file.html',context)
        # if buton == 'Сохранить в БД':
        #     context={
        #         'uploaded_file':uploaded_file,
        #         'hop':t
        #
        #     }
        #     print(context)
        #
        #     st = request.POST.get('uploaded_file')
        #     fin = request.POST.get('hop')
        #     obj = Articles()
        #     obj.start = st
        #     obj.finish = fin
        #     obj.save()

            return render(request, 'news/file.html',context)
        # if buton == 'Сохранить в БД':
        #     context={
        #         'uploaded_file':uploaded_file,
        #         'hop':t
        #
        #     }
        #     print(context)
        #
        #     st = request.POST.get('uploaded_file')
        #     fin = request.POST.get('hop')
        #     obj = Articles()
        #     obj.start = st
        #     obj.finish = fin
        #     obj.save()

            # return render(request, 'news/file.html',context)


    return render(request, 'news/file.html',context)

# def fileload(request):
#     button = request.POST.get('button')
#     buton = request.POST.get('acction')
#
#     if request.method == 'POST' and buton=='Обработать':
#             print('fil')
#             return render(request, 'news/fileload.html')
#     return render(request, 'news/fileload.html')

            # bulkemails = q
            #
            #
            # segmenter = Segmenter()
            # morph_vocab = MorphVocab()
            # emb = NewsEmbedding()
            # morph_tagger = NewsMorphTagger(emb)
            # syntax_parser = NewsSyntaxParser(emb)
            # ner_tagger = NewsNERTagger(emb)
            # names_extractor = NamesExtractor(morph_vocab)
            #
            # doc = Doc(bulkemails)
            # doc.segment(segmenter)
            #
            # doc.tag_morph(morph_tagger)
            # doc.parse_syntax(syntax_parser)
            # doc.tag_ner(ner_tagger)
            # for token in doc.tokens:
            #     token.lemmatize(morph_vocab)
            # for span in doc.spans:
            #     span.normalize(morph_vocab)
            # fio = ''
            # for span in doc.spans:
            #     if span.type == PER:
            #         span.extract_fact(names_extractor)
            # names_dict = {_.normal: _.fact.as_dict for _ in doc.spans if _.fact}
            # for key in names_dict:
            #     fio +=(key)
            #
            #
            # r = re.compile('')
            # t = re.sub(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)','x',bulkemails)
            # t = re.sub(r'(\b\+?[7,8](\s*\d{3}\s*\d{3}\s*\d{2}\s*\d{2})\b)','x',t)
            # t = re.sub(r'(\d{4}[\s\-]*\d{4}[\s\-]*\d{4}[\s\-]*\d{4})','x',t)
            # #дата
            # t = re.sub(r'(\d{2}.\d{2}.\d{4}\s\года\s\рождения)','x',t)
            # t = re.sub(r'(родившийся\s\d{2}.\d{2}.\d{4}\s\года)','x',t)
            # t = re.sub(r'(дата\s\рождения\s\d{2}.\d{2}.\d{4})','x',t)
            # # t = re.sub(r'(\d{2}-\d{2}-\d{4})','x'+cr,t)
            # #серия паспорта
            # t = re.sub(r'(\b\w{5}\b\s\d{4}\b)','x',t)
            # #номер паспорта
            # t = re.sub(r'(\b\w{5}\b\s\d{6}\b)','x',t)
            # #адресу
            # t = re.sub(r'(улица\s\w+\b)','x',t)
            # t = re.sub(r'(ул.\s\w+\b)','x',t)
            # t = re.sub(r'(дом\s\d+\b)','x',t)
            # t = re.sub(r'(д.\s\d+\b)','x',t)
            # #фио
            # t = re.sub(r'([А-Я][а-я]+\s+[А-Я]\.[А-Я]\.)','x',t)
            # t = re.sub(r'([А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+\s)','x',t)
            # t = re.sub(r'([А-Я][а-я]+\s+[А-Я][а-я]+\s+[А-Я][а-я]+[,])','x',t)
            #
            #
            # results = r.findall(bulkemails)
            # emails = ""
            # for x in results:
            #         emails += str(x)+"\n"
            # context={
            #     'hop':t
            # }
def baza(request):
    obj = Articles()
    vse=Articles.objects.all()

    context={
        'baz':vse
    }
    return render(request, 'news/baza.html',context)
