import sys

from django.shortcuts import render
# from CraftManagerApp.forms import *
from craft_manager_app.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView, FormView, CreateView, UpdateView


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class LabListView(ListView):
    model = LabStation

    template_name = "lab_list.html"
    context_object_name = "labs"

    def get_queryset(self):
        return LabStation.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewCraftView(View):
    def get(self, request):
        labs = LabStation.objects.all()
        return render(request, "new_craft.html", context={"labs": labs})

    def post(self, request):
        lab_name = request.POST.get("lab")
        item_name = request.POST.get("item")
        is_craft_failed = False

        print(f"{lab_name} - {item_name}", file=sys.stderr)

        lab_station = LabStation.objects.filter(name=lab_name).first()

        if lab_station.flat_flask > 0:
            lab_station.flat_flask -= 1
        else:
            is_craft_failed = True

        if lab_station.pipette > 0:
            lab_station.pipette -= 1
        else:
            is_craft_failed = True

        if lab_station.test_tube > 0:
            lab_station.test_tube -= 1
        else:
            is_craft_failed = True

        match item_name:
            case "antidotum":
                if lab_station.conical_flask > 0:
                    lab_station.conical_flask -= 1
                else:
                    is_craft_failed = True

            case "antybiotyk":
                pass

            case "hypno":
                if lab_station.conical_flask > 0:
                    lab_station.conical_flask -= 1
                else:
                    is_craft_failed = True

                if lab_station.crystalizer > 0:
                    lab_station.crystalizer -= 1
                else:
                    is_craft_failed = True

                if lab_station.high_cylinder_with_plug > 0:
                    lab_station.high_cylinder_with_plug -= 1
                else:
                    is_craft_failed = True

                if lab_station.cylinder_with_spigot > 0:
                    lab_station.cylinder_with_spigot -= 1
                else:
                    is_craft_failed = True

                if lab_station.petri_dish > 0:
                    lab_station.petri_dish -= 1
                else:
                    is_craft_failed = True

            case "med_x":
                pass

            case "narkotyk":
                if lab_station.threaded_bottle > 0:
                    lab_station.threaded_bottle -= 1
                else:
                    is_craft_failed = True

                if lab_station.beaker > 0:
                    lab_station.beaker -= 1
                else:
                    is_craft_failed = True

            case "radaway":
                if lab_station.cylinder_with_spigot > 0:
                    lab_station.cylinder_with_spigot -= 1
                else:
                    is_craft_failed = True

                if lab_station.funnel > 0:
                    lab_station.funnel -= 1
                else:
                    is_craft_failed = True

                if lab_station.watch_glass > 0:
                    lab_station.watch_glass -= 1
                else:
                    is_craft_failed = True

            case "rad_x":
                if lab_station.threaded_bottle > 0:
                    lab_station.threaded_bottle -= 1
                else:
                    is_craft_failed = True

                if lab_station.funnel > 0:
                    lab_station.funnel -= 1
                else:
                    is_craft_failed = True

                if lab_station.watch_glass > 0:
                    lab_station.watch_glass -= 1
                else:
                    is_craft_failed = True

            case "serum_prawdy":
                if lab_station.conical_flask > 0:
                    lab_station.conical_flask -= 1
                else:
                    is_craft_failed = True

                if lab_station.crystalizer > 0:
                    lab_station.crystalizer -= 1
                else:
                    is_craft_failed = True

                if lab_station.high_cylinder_with_plug > 0:
                    lab_station.high_cylinder_with_plug -= 1
                else:
                    is_craft_failed = True

            case "stimpak":
                if lab_station.beaker > 0:
                    lab_station.beaker -= 1
                else:
                    is_craft_failed = True

                if lab_station.funnel > 0:
                    lab_station.funnel -= 1
                else:
                    is_craft_failed = True

                if lab_station.petri_dish > 0:
                    lab_station.petri_dish -= 1
                else:
                    is_craft_failed = True

            case "sstimpak":
                if lab_station.crystalizer > 0:
                    lab_station.crystalizer -= 1
                else:
                    is_craft_failed = True

                if lab_station.funnel > 0:
                    lab_station.funnel -= 1
                else:
                    is_craft_failed = True

                if lab_station.petri_dish > 0:
                    lab_station.petri_dish -= 1
                else:
                    is_craft_failed = True

            case "szpryca":
                pass

            case "spiulkolot":
                if lab_station.beaker > 0:
                    lab_station.beaker -= 1
                else:
                    is_craft_failed = True

                if lab_station.funnel > 0:
                    lab_station.funnel -= 1
                else:
                    is_craft_failed = True

            case "trucizna":
                if lab_station.cylinder_with_spigot > 0:
                    lab_station.cylinder_with_spigot -= 1
                else:
                    is_craft_failed = True

                if lab_station.beaker > 0:
                    lab_station.beaker -= 1
                else:
                    is_craft_failed = True

        lab_station.save()

        if is_craft_failed:
            return redirect("/craft_failed/")
        else:
            return redirect("/craft_success/")


class CraftFailedView(View):
    def get(self, request):
        return render(request, "craft_failed.html")


class CraftSuccessView(View):
    def get(self, request):
        return render(request, "craft_success.html")


class AccreditationView(View):
    def get(self, request):
        labs = LabStation.objects.all()
        return render(request, "accreditation.html", context={"labs": labs})

    def post(self, request):
        lab_name = request.POST.get("lab")
        item_name = request.POST.get("item")
        vitality = int(request.POST.get("vitality"))

        # lab_station = LabStation.objects.get(name=lab_name)
        print(f"{lab_name} - {item_name} - {vitality}", file=sys.stderr)

        lab_station = LabStation.objects.filter(name=lab_name).first()

        match item_name:
            case "flat_flask":
                lab_station.flat_flask += 4
            case "flat_flask500":
                lab_station.flat_flask += 8
            case "conical_flask200":
                lab_station.conical_flask += 2
            case "conical_flask200500":
                lab_station.conical_flask += 4
            case "conical_flask500":
                lab_station.conical_flask += 8
            case "pipette":
                lab_station.pipette += 2
            case "test_tube":
                lab_station.test_tube += 1
            case "beaker100":
                lab_station.beaker += 2
            case "beaker100250":
                lab_station.beaker += 4
            case "beaker250":
                lab_station.beaker += 8
            case "threaded_bottle200":
                lab_station.threaded_bottle += 2
            case "threaded_bottle200500":
                lab_station.threaded_bottle += 4
            case "threaded_bottle500":
                lab_station.threaded_bottle += 8
            case "cylinder_with_spigot":
                lab_station.cylinder_with_spigot += 10
            case "crystalizer":
                lab_station.crystalizer += 6
            case "funnel":
                lab_station.funnel += 6
            case "petri_dish":
                lab_station.petri_dish += 6
            case "watch_glass":
                lab_station.watch_glass += 6
            case "high_cylinder_with_plug":
                lab_station.high_cylinder_with_plug += 4

        lab_station.save()

        return redirect("/accreditation_success/")


class AccreditationSuccessView(View):
    def get(self, request):
        return render(request, "accreditation_success.html")