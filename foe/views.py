# -*- coding: utf-8 -*-

from django.shortcuts import redirect, render, render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import *
from .models import *
from django.utils.text import slugify

#
# FOE, main site
#


def index(request):
    args = dict()
    return render_to_response('foe/main/index.html', args)


@login_required
def registro_oe(request):
    args = dict()
    usuario = request.user
    oe_usuario = OrganizacionEstudiantil(usuario=usuario)
    oe = OrganizacionEstudiantil.objects.filter(usuario=usuario)
    args['completo'] = False

    if request.method == 'POST':
        print(usuario)
        if oe:
            form = OEForm(request.POST, request.FILES, instance=oe[0])
        else:
            form = OEForm(request.POST, request.FILES, instance=oe_usuario)
        if form.is_valid():
            f = form.save()
            f.slug = slugify(f.nombre)
            f.save()
            return redirect(reverse('registro_bancario'))

    else:
        if oe:
            form = OEForm(instance=oe[0])
        else:
            form = OEForm(instance=oe_usuario)
    args['form'] = form
    return render(request, "foe/forms/registroOE.html", args)


@login_required
def registro_comite(request):
    args = dict()
    usuario = request.user
    cm_usuario = Comite(usuario=usuario)
    cm = Comite.objects.filter(usuario=usuario)

    if request.method == 'POST':
        print(usuario)
        if cm:
            form = ComiteForm(request.POST, request.FILES, instance=cm[0])
        else:
            form = ComiteForm(request.POST, request.FILES, instance=cm_usuario)
        print(request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        if cm:
            form = ComiteForm(instance=cm[0])
        else:
            form = ComiteForm(instance=cm_usuario)
    args['form'] = form
    return render(request, "foe/forms/comite.html", args)


@login_required
def miembros_oe(request):
    args = dict()
    usuario = request.user
    oe = get_object_or_404(OrganizacionEstudiantil, usuario=usuario)
    pres_oe = Miembro(organizacion_estudiantil=oe,
                      cargo='presidente')
    pres = Miembro.objects.filter(organizacion_estudiantil=oe,
                                  cargo='presidente')
    sec_oe = Miembro(organizacion_estudiantil=oe,
                     cargo='secretario')
    sec = Miembro.objects.filter(
        organizacion_estudiantil=oe,
        cargo='secretario')
    tes_oe = Miembro(
        organizacion_estudiantil=oe,
        cargo='tesorero')
    tes = Miembro.objects.filter(
        organizacion_estudiantil=oe,
        cargo='tesorero')
    redes_oe = Miembro(
        organizacion_estudiantil=oe,
        cargo='redes')
    redes = Miembro.objects.filter(
        organizacion_estudiantil=oe,
        cargo='redes')

    if request.method == 'POST':
        if pres:
            form_presidente = MiembroForm(
                request.POST,
                request.FILES,
                instance=pres[0],
                prefix='presidente')
        else:
            form_presidente = MiembroForm(
                request.POST,
                request.FILES,
                instance=pres_oe,
                prefix='presidente')

        if sec:
            form_secretario = MiembroForm(
                request.POST,
                request.FILES,
                instance=sec[0],
                prefix='secretario')
        else:
            form_secretario = MiembroForm(
                request.POST,
                request.FILES,
                instance=sec_oe,
                prefix='secretario')

        if tes:
            form_tesorero = MiembroForm(
                request.POST,
                request.FILES,
                instance=tes[0],
                prefix='tesorero')
        else:
            form_tesorero = MiembroForm(
                request.POST,
                request.FILES,
                instance=tes_oe,
                prefix='tesorero')

        if redes:
            form_redes = MiembroForm(
                request.POST,
                request.FILES,
                instance=redes[0],
                prefix='redes')
        else:
            form_redes = MiembroForm(
                request.POST,
                request.FILES,
                instance=redes_oe,
                prefix='redes')
            
        if form_presidente.is_valid():
            form_presidente.save()
        if form_secretario.is_valid():
            form_secretario.save()
        if form_tesorero.is_valid():
            form_tesorero.save()
        if form_redes.is_valid():
            form_redes.save()
            return redirect('/')

    else:
        if pres:
            form_presidente = MiembroForm(
                instance=pres[0],
                prefix='presidente')
        else:
            form_presidente = MiembroForm(
                instance=pres_oe,
                prefix='presidente')

        if sec:
            form_secretario = MiembroForm(
                instance=sec[0],
                prefix='secretario')
        else:
            form_secretario = MiembroForm(
                instance=sec_oe,
                prefix='secretario')

        if tes:
            form_tesorero = MiembroForm(
                instance=tes[0],
                prefix='tesorero')
        else:
            form_tesorero = MiembroForm(
                instance=tes_oe,
                prefix='tesorero')

        if redes:
            form_redes = MiembroForm(
                instance=redes[0],
                prefix='redes')
        else:
            form_redes = MiembroForm(
                instance=redes_oe,
                prefix='redes')

    args['form_presidente'] = form_presidente
    args['form_secretario'] = form_secretario
    args['form_tesorero'] = form_tesorero
    args['form_redes'] = form_redes

    return render(request, "foe/forms/miembro.html", args)


@login_required
def datos_bancarios(request):
    args = dict()
    usuario = request.user
    oe = get_object_or_404(OrganizacionEstudiantil, usuario=usuario)
    m_oe = DatosBancarios(organizacion_estudiantil=oe)
    m = DatosBancarios.objects.filter(organizacion_estudiantil=oe)

    if request.method == 'POST':
        print(usuario)
        if m:
            form = BancarioForm(request.POST, request.FILES, instance=m[0])
        else:
            form = BancarioForm(request.POST, request.FILES, instance=m_oe)
        if form.is_valid():
            form.save()
            return redirect(reverse('registro_miembro'))

    else:
        if m:
            form = BancarioForm(instance=m[0])
        else:
            form = BancarioForm(instance=m_oe)
    args['form'] = form
    return render(request, "foe/forms/datos-bancarios.html", args)


def directorio(request):
    args = dict()
    oes = OrganizacionEstudiantil.objects.all()
    oes.order_by('clasificacion', 'nombre')
    args['organizaciones'] = oes
    return render(request, "foe/main/directorio.html", args)


def perfil_oe(request, oe_slug):
    args = dict()
    oe = get_object_or_404(
        OrganizacionEstudiantil, slug=oe_slug)
    args['oe'] = oe
    args['logo_url'] = oe.logo._get_url()
    args['plan_trabajo_url'] = oe.plan_trabajo._get_url()
    args['presupuesto_url'] = oe.presupuesto._get_url()
    return render(request, "foe/main/perfil.html", args)
