import DataTech
import shutil
from templates.TemplateLocalisation import localisationStart, localisationTechTemplate
from templates.TemplateTech import techStart, techTemplate, techProgCost
from Utility import writeToFile, languages

def createTech():
    techText = techStart
    for tech in DataTech.techs:
        type = tech["name"]
        area = tech["area"]
        cost = tech["cost"]
        if cost == 0:
            cost = techProgCost
        category = tech["category"]
        for i in range(tech["tiers"]):
            techText = techText + techTemplate.format(type = type, num = i+1, area = area, category = category, cost = cost)
    writeToFile("common/technology/archipelago_progressive_tech.txt",techText)

def createTechLocalisations():
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for tech in DataTech.techs:
            type = tech["name"]
            name = type[0].upper() + type[1:]
            for i in range(tech["tiers"]):
                if i+1 == tech["tiers"]:
                    final = "final"
                else:
                    final = "next"
                localisationText = localisationText + localisationTechTemplate.format(type = type, num = i+1, name = name, final = final)
        writeToFile("localisation/" + lang + "/archipelago_progressive_techs_l_" + lang + ".yml", localisationText,"utf-8-sig")

def createTechIcons():
    path = "mod/testresource/gfx/interface/icons/technologies/"
    iconTempName = "tech_progressive"
    iconFinName = iconTempName+"_{type}_{num}"
    format = ".dds"
    for tech in DataTech.techs:
        type = tech["name"]
        for i in range(tech["tiers"]):
            iconFinal = iconFinName.format(type = type,num = i+1)+format
            shutil.copyfile(path+iconTempName+format,path+iconFinal)