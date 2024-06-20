from tkinter import *
import json
import time
import math
import os

#----------------- Dictionaries
slot_type_weight = {}
type_modif = {}
type_total = {}
#---------------
charge_check = []
top_2_list = []

def Boot_Loader():
   global slot_type_weight
   global type_modif
   global type_total
   
   type_modif = {"normal": 0.2,
                "metal": 0.5,
                "ghost": 1.0,
                "wood": 1.0,
                "ice": 1.0,
                "ground": 1.0,
                "fire": 1.0,
                "flying": 1.0,
                "water": 1.0,
                "dragon": 1.0,
                "demon": 1.0,
                "grass": 1.0,
                "poison": 1.0,
                "fighting": 1.0,
                "bug": 1.0,
                "dark": 1.0,
                "rock": 1.0,
                "charge": 1.0
                }
   
   file_type_modif = 'type_modif.json'
   with open(file_type_modif, 'w') as f_tp_md:
      json.dump(type_modif, f_tp_md)    

   slot_type_weight = {"helmet" : {"type" : "normal" , "weight" : 1.5},
                    "cape" : {"type"  : "normal" , "weight" : 1.0 },
                    "amulet" : {"type" : "normal" , "weight" : 1.0},
                    "quiver" : {"type" : "normal" , "weight" : 1.0},
                    "platebody" : {"type" : "normal" , "weight" : 1.7},
                    "platelegs" : {"type" : "normal" , "weight" : 1.5},
                    "weapon" : {"type" : "normal" , "weight" : 2.0},
                    "shield" : {"type" : "normal" , "weight" : 1.6},
                    "gloves" : {"type" : "normal" , "weight" : 1.3},
                    "boots" : {"type" : "normal" , "weight" : 1.2},
                    "ring" : {"type" : "normal" , "weight" : 1.5}
                    }
   
   file_slot_type_weight = 'slot_type_weight.json'
   with open(file_slot_type_weight, 'w') as f_st_tp_wg:
      json.dump(slot_type_weight, f_st_tp_wg) 
      
   type_total = {"normal": 3.0,
                "metal": 0.0,
                "ghost": 0.0,
                "wood": 0.0,
                "ice": 0.0,
                "ground": 0.0,
                "fire": 0.0,
                "flying": 0.0,
                "water": 0.0,
                "dragon": 0.0,
                "demon": 0.0,
                "grass": 0.0,
                "poison": 0.0,
                "fighting": 0.0,
                "bug": 0.0,
                "dark": 0.0,
                "rock": 0.0,
                "charge": 0.0
                }
   
   file_type_total = 'type_total.json'
   with open(file_type_total, 'w') as f_tp_t:
      json.dump(type_total, f_tp_t)    

#def color_maps(color_type):
   #if color_type == "normal":
      #return "Red"
   #elif color_type == "metal":
      #return "Blue"
   #elif color_type == "ghost":
      #return "Green"
   #elif color_type == "wood":
      #return "Red"
   #elif color_type == "ice":
      #return "Pink"
   #elif color_type == "ground":
      #return "White"
   #elif color_type == "fire":
      #return "White"
   #elif color_type == "flying":
      #return "White"
   #elif color_type == "water":
      #return "White"
   #elif color_type == "dragon":
      #return "White"
   #elif color_type == "demon":
      #return "White"
   #elif color_type == "grass":
      #return "White"
   #elif color_type == "poison":
      #return "White"
   #elif color_type == "fighting":
      #return "White"
   #elif color_type == "bug":  
      #return "White"
   #elif color_type == "dark":
      #return "White"
   #elif color_type == "rock":
      #return "White"
   #else:   
      #return "White"
   
#def change_color(slot):
      #global slot_type_weight
      #if slot == "helmet":
         #return color_maps(slot_type_weight["helmet"]["type"])
      #elif slot == "cape":
         #return color_maps(slot_type_weight["cape"]["type"])
      
def sets_type():
   #--------------------------- Type Sets
   text_helmet.set(slot_type_weight["helmet"]["type"])
   text_cape.set(slot_type_weight["cape"]["type"])
   text_amulet.set(slot_type_weight["amulet"]["type"])
   text_quiver.set(slot_type_weight["quiver"]["type"])
   text_platebody.set(slot_type_weight["platebody"]["type"])
   text_platelegs.set(slot_type_weight["platelegs"]["type"])
   text_weapon.set(slot_type_weight["weapon"]["type"])
   text_shield.set(slot_type_weight["shield"]["type"])
   text_gloves.set(slot_type_weight["gloves"]["type"])
   text_boots.set(slot_type_weight["boots"]["type"])
   text_ring.set(slot_type_weight["ring"]["type"])

def sets_weight():
   #--------------------------- Weight
   num_helmet.set(slot_type_weight["helmet"]["weight"])
   num_cape.set(slot_type_weight["cape"]["weight"])
   num_amulet.set(slot_type_weight["amulet"]["weight"])
   num_quiver.set(slot_type_weight["quiver"]["weight"])
   num_platebody.set(slot_type_weight["platebody"]["weight"])
   num_platelegs.set(slot_type_weight["platelegs"]["weight"])
   num_weapon.set(slot_type_weight["weapon"]["weight"])
   num_shield.set(slot_type_weight["shield"]["weight"])
   num_gloves.set(slot_type_weight["gloves"]["weight"])
   num_boots.set(slot_type_weight["boots"]["weight"])
   num_ring.set(slot_type_weight["ring"]["weight"])   


def sets_total_boot():
   #-------------------------- Total boot Setter
   total_normal.set((round(type_total["normal"],1)))
   total_metal.set(round(type_total["metal"],1))
   total_ghost.set(round(type_total["ghost"],1))
   total_wood.set(round(type_total["wood"],1))
   total_ice.set(round(type_total["ice"],1))
   total_ground.set(round(type_total["ground"],1))
   total_fire.set(round(type_total["fire"],1))
   total_flying.set(round(type_total["flying"],1))
   total_water.set(round(type_total["water"],1))
   total_dragon.set(round(type_total["dragon"],1))
   total_demon.set(round(type_total["demon"],1))
   total_grass.set(round(type_total["grass"],1))
   total_poison.set(round(type_total["poison"],1))
   total_fighting.set(round(type_total["fighting"],1))
   total_bug.set(round(type_total["bug"],1))
   total_dark.set(round(type_total["dark"],1))
   total_rock.set(round(type_total["rock"],1))
   total_charge.set(round(type_total["charge"],1))  

#def sets_top2_boot(type_total):
   #count = 0
   #g
   #for count in type_total:
      
      #print(list(type_total.keys())[count] + type_total[count])
     
def sets_top2_boot(type_total):
   eval_list = []
   top1 = None
   top2 = None
   name_top1 = 'Normal'
   name_top2 = 'Normal'
   count = 0
   global top_2_list
   for count in type_total:
      eval_list.append(type_total[count])
   #print(eval_list)
   for i, value in enumerate(eval_list):
      #print(value)
      if top1 is None or value > top1:
         top2 = top1
         name_top2 = name_top1
         top1 = value
         name_top1 = list(type_total.keys())[i]
      elif top2 is None or value > top2:
         top2 = value
         name_top2 = list(type_total.keys())[i]
   if top2 < 1.5:
      name_top2 = name_top1
   top_2_list.append(name_top1)
   top_2_list.append(name_top2)
   top1_type.set(name_top1)
   top2_type.set(name_top2)   
   #print(name_top1)
   #print(name_top2)

#Boot_Loader()
#sets_top2_boot(type_total)
      
def sets_total(slots, modif, type_total, theslot):
   global charge_check
   global slot_type_weight
   global type_modif
   if (-0.15 <= type_total[slots["type"]] <= 0.15):
      type_total[slots["type"]] = 0.0
   if (slots["type"] == "normal" and not(theslot in charge_check)):
      type_total["normal"] += slots["weight"] * modif["normal"]
      #print("n1f: " + str(type_total["normal"]))
   elif (slots["type"] == "normal" and (theslot in charge_check)):
      type_total["charge"] -= slots["weight"]  * modif["charge"]
      type_total["normal"] += slots["weight"] * modif["normal"]
     #print("n1t: " + str(type_total["normal"]))
      charge_check.remove(theslot)
   elif slots["type"] == "metal":
      type_total["normal"] -= slots["weight"]  * modif["normal"]
      type_total["metal"] += slots["weight"] * modif["metal"]
      #print("n2: " + str(type_total["normal"]))
      #print("m3: " + str(type_total["metal"]))
   elif slots["type"] == "ghost":
      type_total["metal"] -= slots["weight"]  * modif["metal"]
      type_total["ghost"] += slots["weight"] * modif["ghost"]
   elif slots["type"] == "wood":
      type_total["ghost"] -= slots["weight"]  * modif["ghost"]
      type_total["wood"] += slots["weight"] * modif["wood"]
   elif slots["type"] == "ice":
      type_total["wood"] -= slots["weight"]  * modif["wood"]
      type_total["ice"] += slots["weight"] * modif["ice"]
   elif slots["type"] == "ground":
      type_total["ice"] -= slots["weight"]  * modif["ice"]
      type_total["ground"] += slots["weight"] * modif["ground"]
   elif slots["type"] == "fire":
      type_total["ground"] -= slots["weight"]  * modif["ground"]
      type_total["fire"] += slots["weight"] * modif["fire"] 
   elif slots["type"] == "flying":
      type_total["fire"] -= slots["weight"]  * modif["fire"]
      type_total["flying"] += slots["weight"] * modif["flying"]
   elif slots["type"] == "water":
      type_total["flying"] -= slots["weight"]  * modif["flying"]
      type_total["water"] += slots["weight"] * modif["water"] 
   elif slots["type"] == "dragon":
      type_total["water"] -= slots["weight"]  * modif["water"]
      type_total["dragon"] += slots["weight"] * modif["dragon"]
   elif slots["type"] == "demon":
      type_total["dragon"] -= slots["weight"]  * modif["dragon"]
      type_total["demon"] += slots["weight"] * modif["demon"]
   elif slots["type"] == "grass":
      type_total["demon"] -= slots["weight"]  * modif["demon"]
      type_total["grass"] += slots["weight"] * modif["grass"]
   elif slots["type"] == "poison":
      type_total["grass"] -= slots["weight"]  * modif["grass"]
      type_total["poison"] += slots["weight"] * modif["poison"]
   elif slots["type"] == "fighting":
      type_total["poison"] -= slots["weight"]  * modif["poison"]
      type_total["fighting"] += slots["weight"] * modif["fighting"] 
   elif slots["type"] == "bug":
      type_total["fighting"] -= slots["weight"]  * modif["fighting"]
      type_total["bug"] += slots["weight"] * modif["bug"]
   elif slots["type"] == "dark":
      type_total["bug"] -= slots["weight"]  * modif["bug"]
      type_total["dark"] += slots["weight"] * modif["dark"]  
   elif slots["type"] == "rock":
      type_total["dark"] -= slots["weight"]  * modif["dark"]
      type_total["rock"] += slots["weight"] * modif["rock"]
      #print("r1: " + str(type_total["rock"]))           
   elif slots["type"] == "charge":
      type_total["rock"] -= slots["weight"]  * modif["rock"]
      type_total["charge"] += slots["weight"] * modif["charge"]
      #print("r2: " + str(type_total["rock"]))
      #print("c1: " + str(type_total["charge"]))
      #print("bf: " + str(charge_check))
      charge_check.append(theslot)
      #print("af: " + str(charge_check))
   #total_normal.set(round(type_total[slots["type"]],2))

   #------------ slots["type"] = "normal" --> type_total["normal"] = valor a atribuir a normal
   #------------ type_slot ---> slot_type_weight["helmet"]) -> {'type': 'normal', 'weight': 1.5} 
   #------------ slots = {"type" : "normal" , "weight" : 1.5}....
   #------------ theslot = "helm"
   #------------ modif = {"normal": 0.2,"metal": 0.5,
   #------------ type total = {"normal": 2.2, "metal": 0.0,
#------------------------------------------------------------------------------------------------------

#def Main():
   #slot_type_weight["helmet"]["type"] = "rock"
   #sets_total(slot_type_weight["helmet"], type_modif, type_total, "helmet")
   #slot_type_weight["helmet"]["type"] = "charge"
   #sets_total(slot_type_weight["helmet"], type_modif, type_total, "helmet")
   #print("inb: " + str(charge_check))
   #slot_type_weight["cape"]["type"] = "charge"
   #sets_total(slot_type_weight["cape"], type_modif, type_total, "cape")
   #print("case1: " + str(charge_check))
   #slot_type_weight["helmet"]["type"] = "normal"
   #print("aft: " + str(charge_check))
   #sets_total(slot_type_weight["helmet"], type_modif, type_total, "helmet")
   #print("aft2: " + str(charge_check))
   #slot_type_weight["helmet"]["type"] = "metal"
   #sets_total(slot_type_weight["helmet"], type_modif, type_total, "helmet")
   #print("c2: " + str(type_total["charge"]))
#Boot_Loader()
#Main()
   
def Slot_Swap(type_slot):
   #print(slot_type_weight)
   #print(type_modif)
   global charge_check
   global slot_type_weight
   global type_modif
   global type_total
   
   types = list(type_modif.keys())  
   slots = list(slot_type_weight.values())
   search = 0
   while type_slot["type"] != types[search]:
      search += 1
   #------------ type_slot ---> slot_type_weight["helmet"]) -> {'type': 'normal', 'weight': 1.5} ...
   #------------ slots = {"type" : "normal" , "weight" : 1.5}....
   #------------ theslot = "helm"
   #------------ modif = {"normal": 0.2,"metal": 0.5,
   #------------ type total = {"normal": 2.2, "metal": 0.0,...
   if (type_slot["type"] == types[-1]):
      type_slot["type"] = types[0]
      sets_total(type_slot, type_modif, type_total, type_slot)
   else:
      type_slot["type"] = types[search + 1]
      sets_total(type_slot, type_modif, type_total, type_slot)
   #print(slot_type_weight)
   sets_type()
   sets_total_boot()
   sets_top2_boot(type_total)

      
def Main_2():
   global slot_type_weight
   global type_modif
   global type_total
   global charge_check
   
   #----------- Frame Setups Equipment Frame
   EquipmentFrame = Canvas(root, width = 950, height = 1000)
   EquipmentFrame.pack(fill ="both", expand = True)
   EquipmentFrame.create_image(0, 0, image = bg_eqF, anchor = "nw")
   EquipmentFrame.propagate(0)
   #-------------------------- Frame Setups of Children of Equipment Frame
   frame_helmet = LabelFrame(EquipmentFrame, text="Helmet", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_cape = LabelFrame(EquipmentFrame, text="Cape", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_amulet = LabelFrame(EquipmentFrame, text="Amulet", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_quiver = LabelFrame(EquipmentFrame, text="Quiver", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_platebody = LabelFrame(EquipmentFrame, text="Platebody", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_platelegs = LabelFrame(EquipmentFrame, text="Platelegs", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_weapon = LabelFrame(EquipmentFrame, text="Weapon", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_shield = LabelFrame(EquipmentFrame, text="Shield", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_gloves = LabelFrame(EquipmentFrame, text="Gloves", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_boots = LabelFrame(EquipmentFrame, text="Boots", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   frame_ring = LabelFrame(EquipmentFrame, text="Ring", bg="LightSalmon3", pady = 20, padx = 50, width = 200, height = 200)
   #------------------------- Frame Setups of Stats Frame
   StatsFrame = LabelFrame(root, text="Stats", bg="grey", width = 900, height = 900)
   StatsFrame.propagate(0)   
   #------------------------- Frame Setup of Children of Stats Frame
   top2_types = Frame(StatsFrame, bg="slategray", bd=2, relief="solid", width = 900, height = 450)
   top2_types.propagate(0)
   bottom_types = Frame(StatsFrame, bg="slategray", bd=2, relief="solid", width = 900, height = 450)
   bottom_types.propagate(0)  
   #------------------------- Frame Setup of Children of Children of Stats Frame
   
   first_type = Frame(top2_types, bg="LightGoldenrod1", bd=2, relief="solid", width = 425, height = 450)
   second_type = Frame(top2_types, bg="LightGoldenrod1", bd=2, relief="solid", width = 425, height = 450)
   
   #------------------------- LabelFrame Setup of 3x Children Stats Frame
   first_labelFrame = LabelFrame(top2_types,text = "Type 1", font = ('Arial', 15 , 'bold'), bg = "lightgrey", width = 225, height = 250)
   first_labelFrame.grid_columnconfigure(0, minsize = 225)
   first_labelFrame.grid_rowconfigure(0, minsize = 225)   
   second_labelFrame = LabelFrame(top2_types,text = "Type 2", font = ('Arial', 15 , 'bold'), bg = "lightgrey", width = 225, height = 250)
   second_labelFrame.grid_columnconfigure(0, minsize = 225)
   second_labelFrame.grid_rowconfigure(0, minsize = 225)     
   #----
   third_labelFrame = LabelFrame(bottom_types,text = "Full Data of Your Current Gear Setup", font = ('Arial', 15 , 'bold'), bg = "lightgrey", width = 900, height = 450)
   third_labelFrame.grid_columnconfigure(0, minsize = 50)
   #------------------------- Labels Setup of 4x Children Stats Frame
   #---------- (TOP) ALL THE LABELS ------------------------------------
   sets_top2_boot(type_total)
   label_top_1st_text = Label(first_labelFrame, textvariable = top1_type, bg = "lightgrey", font = ('Arial', 15 , 'bold'), borderwidth = 0, relief= RAISED, width = 20, height = 0)
   label_top_2nd_text = Label(second_labelFrame, textvariable = top2_type, bg = "lightgrey", font = ('Arial', 15 , 'bold'), borderwidth = 0, relief= RAISED, width = 20, height = 0)
   #---------- (BOTTOM) ALL THE LABELS ---------------------------------
   sets_total_boot()
   label_btm_normal_text = Label(third_labelFrame, bg = "lightgrey", text = "Normal: ",font = ('Arial', 12 , 'bold'))
   label_btm_normal = Label(third_labelFrame, bg = "lightgrey", textvariable = total_normal,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_metal_text = Label(third_labelFrame, bg = "lightgrey", text = "Metal: ",font = ('Arial', 12 , 'bold'))
   label_btm_metal = Label(third_labelFrame, bg = "lightgrey", textvariable= total_metal,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_ghost_text = Label(third_labelFrame, bg = "lightgrey", text = "Ghost: ",font = ('Arial', 12 , 'bold'))
   label_btm_ghost = Label(third_labelFrame, bg = "lightgrey", textvariable= total_ghost,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_wood_text = Label(third_labelFrame, bg = "lightgrey", text = "Wood: ",font = ('Arial', 12 , 'bold'))
   label_btm_wood = Label(third_labelFrame, bg = "lightgrey", textvariable= total_wood,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_ice_text = Label(third_labelFrame, bg = "lightgrey", text = "Ice: ",font = ('Arial', 12 , 'bold'))
   label_btm_ice = Label(third_labelFrame, bg = "lightgrey", textvariable= total_ice,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_ground_text = Label(third_labelFrame, bg = "lightgrey", text = "Ground: ",font = ('Arial', 12 , 'bold'))
   label_btm_ground = Label(third_labelFrame, bg = "lightgrey", textvariable= total_ground,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_fire_text = Label(third_labelFrame, bg = "lightgrey", text = "Fire: ",font = ('Arial', 12 , 'bold'))
   label_btm_fire = Label(third_labelFrame, bg = "lightgrey", textvariable= total_fire,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_flying_text = Label(third_labelFrame, bg = "lightgrey", text = "Flying: ",font = ('Arial', 12 , 'bold'))
   label_btm_flying = Label(third_labelFrame, bg = "lightgrey", textvariable= total_flying,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_water_text = Label(third_labelFrame, bg = "lightgrey", text = "Water: ",font = ('Arial', 12 , 'bold'))
   label_btm_water = Label(third_labelFrame, bg = "lightgrey", textvariable= total_water,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_dragon_text = Label(third_labelFrame, bg = "lightgrey", text = "Dragon: ",font = ('Arial', 12 , 'bold'))
   label_btm_dragon = Label(third_labelFrame, bg = "lightgrey", textvariable= total_dragon,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_demon_text = Label(third_labelFrame, bg = "lightgrey", text = "Demon: ",font = ('Arial', 12 , 'bold'))
   label_btm_demon = Label(third_labelFrame, bg = "lightgrey", textvariable= total_demon,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_grass_text = Label(third_labelFrame, bg = "lightgrey", text = "Grass: ",font = ('Arial', 12 , 'bold'))
   label_btm_grass = Label(third_labelFrame, bg = "lightgrey", textvariable= total_grass,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_poison_text = Label(third_labelFrame, bg = "lightgrey", text = "Poison: ",font = ('Arial', 12 , 'bold'))
   label_btm_poison = Label(third_labelFrame, bg = "lightgrey", textvariable= total_poison,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_fighting_text = Label(third_labelFrame, bg = "lightgrey", text = "Fighting: ",font = ('Arial', 12 , 'bold'))
   label_btm_fighting = Label(third_labelFrame, bg = "lightgrey", textvariable= total_fighting,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_bug_text = Label(third_labelFrame, bg = "lightgrey", text = "Bug: ",font = ('Arial', 12 , 'bold'))
   label_btm_bug = Label(third_labelFrame, bg = "lightgrey", textvariable= total_bug,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_dark_text = Label(third_labelFrame, bg = "lightgrey", text = "Dark: ",font = ('Arial', 12 , 'bold'))
   label_btm_dark = Label(third_labelFrame, bg = "lightgrey", textvariable= total_dark,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_rock_text = Label(third_labelFrame, bg = "lightgrey", text = "Rock: ",font = ('Arial', 12 , 'bold'))
   label_btm_rock = Label(third_labelFrame, bg = "lightgrey", textvariable= total_rock,font = ('Arial', 12 , 'bold'))
   #-
   label_btm_charge_text = Label(third_labelFrame, bg = "lightgrey", text = "Charge: ",font = ('Arial', 12 , 'bold'))
   label_btm_charge = Label(third_labelFrame, bg = "lightgrey", textvariable= total_charge,font = ('Arial', 12 , 'bold'))
   #---------- Buttons of Children of Children of Equipement Frame
   
   helmet_b1 = Button(frame_helmet, text= "Helmet", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["helmet"] : Slot_Swap(m))
   cape_b2 = Button(frame_cape, text= "Cape", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["cape"] : Slot_Swap(m))
   amulet_b3= Button(frame_amulet, text= "Amulet", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["amulet"] : Slot_Swap(m))
   quiver_b4= Button(frame_quiver, text= "Quiver", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["quiver"] : Slot_Swap(m))
   platebody_b5= Button(frame_platebody, text= "Platebody", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["platebody"] : Slot_Swap(m))
   platelegs_b6= Button(frame_platelegs, text= "Platelegs", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["platelegs"] : Slot_Swap(m))
   weapon_b7= Button(frame_weapon, text= "Weapon", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["weapon"] : Slot_Swap(m))
   shield_b8= Button(frame_shield, text= "Shield", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["shield"] : Slot_Swap(m))
   gloves_b9= Button(frame_gloves, text= "Gloves", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["gloves"] : Slot_Swap(m))
   boots_b10= Button(frame_boots, text= "Boots", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["boots"] : Slot_Swap(m))
   ring_b11= Button(frame_ring, text= "Ring", font = ('Arial', 15 , 'bold'), bg="AntiqueWhite4", activebackground="AntiqueWhite2", command = lambda m = slot_type_weight["ring"] : Slot_Swap(m))
   
   #------- Secondary Label Boxes Children of Children of Equipement Frame Frame (Output Info)
   sets_type()
   label_helmet = Label(frame_helmet, textvariable = text_helmet, font = ('Arial', 15 , 'bold'), bg="LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)
   label_cape = Label(frame_cape, textvariable = text_cape, font = ('Arial', 15 , 'bold'), bg="LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_amulet = Label(frame_amulet, textvariable = text_amulet, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2" , borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_quiver = Label(frame_quiver, textvariable = text_quiver, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_platebody = Label(frame_platebody, textvariable = text_platebody, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_platelegs = Label(frame_platelegs, textvariable = text_platelegs, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_weapon = Label(frame_weapon, textvariable = text_weapon, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_shield = Label(frame_shield, textvariable = text_shield, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_gloves = Label(frame_gloves, textvariable = text_gloves, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_boots = Label(frame_boots, textvariable = text_boots, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   label_ring = Label(frame_ring, textvariable = text_ring, font = ('Arial', 15 , 'bold'), bg = "LightSalmon2", borderwidth = 0, relief= RAISED, width = 7, height = 0)  
   
   #-------- Position of Equipment Frame on the Grid
   EquipmentFrame.grid(column = 0, row = 0, sticky = EW, pady = 10, padx = 10)
   
   #-------- Position of Children of Equipment Frame on the Grid
   frame_helmet.grid(row = 0, column = 1, pady = 10, padx = 10)  
   frame_cape.grid(row = 1, column = 0, pady = 10, padx = 10) 
   frame_amulet.grid(row = 1, column = 1, pady = 10, padx = 10) 
   frame_quiver.grid(row = 1, column = 2, pady = 10, padx = 10) 
   frame_platebody.grid(row = 2, column = 1, pady = 10, padx = 10) 
   frame_platelegs.grid(row = 3, column = 1, pady = 10, padx = 10) 
   frame_weapon.grid(row = 2, column = 0, pady = 10, padx = 10) 
   frame_shield.grid(row = 2, column = 2, pady = 10, padx = 10) 
   frame_gloves.grid(row = 4, column = 0, pady = 10, padx = 10) 
   frame_boots.grid(row = 4, column = 1, pady = 10, padx = 10) 
   frame_ring.grid(row = 4, column = 2, pady = 10, padx = 10)
   
   #-------- Position of Stats Frame on the Grid
   StatsFrame.grid(column = 1, row = 0, pady = 10, padx = 10, sticky = EW)
   
   #-------- Position of Children of Stats Frame on the Grid
   top2_types.grid(row = 0, pady = 10, padx = 10, sticky = N)
   bottom_types.grid(row = 1, pady = 10, padx = 10, sticky = N)
   
   #-------- Position of Children of Children of Stats Frame on the Grid
   first_type.grid(row = 0, column = 0, pady = 5, padx = 5, sticky = N)
   second_type.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = N)
   
   #-------- Position of 3x Children of Stats Frame on the Grid
   first_labelFrame.grid(row = 0, column = 0, pady = 5, padx = 5)
   second_labelFrame.grid(row = 0, column = 1, pady = 5, padx = 5)
   #--------
   third_labelFrame.grid(pady = 5, padx = 5)
   #-------- Position of 4x Children of Stats Frame on the Grid
   #-------- (TOP) Best 2 Types ---------------------------------------------
   label_top_1st_text.grid(row = 0, column = 0, pady = 5, padx = 5)
   ##--------
   label_top_2nd_text.grid(row = 0, column = 0, pady = 5, padx = 5)
   #--------------------------- (BOTTOM) FULL STATS ---------------------------
   label_btm_normal_text.grid(row = 0, column = 0, pady = 5, padx = 5) 
   label_btm_normal.grid(row = 0, column = 1, pady = 5, padx = 25)
   #-
   label_btm_metal_text.grid(row = 1, column = 0, pady =5, padx = 5)
   label_btm_metal.grid(row = 1, column= 1, pady = 5, padx = 25)
   #-
   label_btm_ghost_text.grid(row = 2, column = 0, pady =5, padx = 5)
   label_btm_ghost.grid(row = 2,column= 1, pady = 5, padx = 25)
   #-
   label_btm_wood_text.grid(row = 3, column = 0, pady =5, padx = 5)
   label_btm_wood.grid(row = 3, column= 1, pady = 5, padx = 25)
   #-
   label_btm_ice_text.grid(row = 4, column = 0, pady =5, padx = 5)
   label_btm_ice.grid(row = 4, column= 1, pady = 5, padx = 25)
   #-
   label_btm_ground_text.grid(row = 5, column = 0, pady =5, padx = 5)
   label_btm_ground.grid(row = 5, column= 1, pady = 5, padx = 25)
   #-
   label_btm_fire_text.grid(row = 6, column = 0, pady =5, padx = 5)
   label_btm_fire.grid(row = 6, column= 1, pady = 5, padx = 25)
   #-
   label_btm_flying_text.grid(row = 7, column = 0, pady =5, padx = 5)
   label_btm_flying.grid(row = 7, column= 1, pady = 5, padx = 25)
   #------------------------------------------------------------------------
   label_btm_water_text.grid(row = 8, column = 0, pady =5, padx = 5)
   label_btm_water.grid(row = 8, column= 1, pady = 5, padx = 25)
   #-
   label_btm_dragon_text.grid(row = 0, column = 2, pady =5, padx = 5)
   label_btm_dragon.grid(row = 0, column= 3, pady = 5, padx = 25)
   #-
   label_btm_demon_text.grid(row = 1, column = 2, pady =5, padx = 5)
   label_btm_demon.grid(row = 1, column= 3, pady = 5, padx = 25)
   #-
   label_btm_grass_text.grid(row = 2, column = 2, pady =5, padx = 5)
   label_btm_grass.grid(row = 2, column= 3, pady = 5, padx = 25)
   #-
   label_btm_poison_text.grid(row = 3, column = 2, pady =5, padx = 5)
   label_btm_poison.grid(row = 3, column= 3, pady = 5, padx = 25)
   #-
   label_btm_fighting_text.grid(row = 4, column = 2, pady =5, padx = 5)
   label_btm_fighting.grid(row = 4,column= 3, pady = 5, padx = 25)
   #-
   label_btm_bug_text.grid(row = 5, column = 2, pady =5, padx = 5)
   label_btm_bug.grid(row = 5, column= 3, pady = 5, padx = 25)
   #-
   label_btm_dark_text.grid(row = 6, column = 2, pady =5, padx = 5)
   label_btm_dark.grid(row = 6, column= 3, pady = 5, padx = 25)
   #-
   label_btm_rock_text.grid(row = 7, column = 2, pady =5, padx = 5)
   label_btm_rock.grid(row = 7, column= 3, pady = 5, padx = 25)
   #-
   label_btm_charge_text.grid(row = 8, column = 2, pady =5, padx = 5)
   label_btm_charge.grid(row = 8, column= 3, pady = 5, padx = 25)
   #-------- Position of Buttons of Children of Children of Equipment Frame on the Grid
   helmet_b1.grid(row = 0, pady = 10)
   cape_b2.grid(row = 0, pady = 10, sticky = EW)
   amulet_b3.grid(row = 0, pady = 10, sticky = EW)
   quiver_b4.grid(row = 0, pady = 10, sticky = EW)
   platebody_b5.grid(row = 0, pady = 10, sticky = EW)
   platelegs_b6.grid(row = 0, pady = 10, sticky = EW)
   weapon_b7.grid(row = 0, pady = 10, sticky = EW)
   shield_b8.grid(row = 0, pady = 10, sticky = EW)
   gloves_b9.grid(row = 0, pady = 10, sticky = EW)
   boots_b10.grid(row = 0, pady = 10, sticky = EW)
   ring_b11.grid(row = 0, pady = 10, sticky = EW)
   
   #-------- Position of Output Labels of Children of Children of Equipment Frame on the Grid
   label_helmet.grid(row = 1, padx = 10, pady = 10)
   label_cape.grid(row = 1, padx = 10, pady = 10)
   label_amulet.grid(row = 1, padx = 10, pady = 10)
   label_quiver.grid(row = 1, padx = 10, pady = 10)
   label_platebody.grid(row = 1, padx = 10, pady = 10)
   label_platelegs.grid(row = 1, padx = 10, pady = 10)
   label_weapon.grid(row = 1, padx = 10, pady = 10)
   label_shield.grid(row = 1, padx = 10, pady = 10)
   label_gloves.grid(row = 1, padx = 10, pady = 10)
   label_boots.grid(row = 1, padx = 10, pady = 10)
   label_ring.grid(row = 1, padx = 10, pady = 10)
   
   #------- Run Root and all its Dependencies in a loop
   root.mainloop()
#------------------------------- Programa (Janela)
root = Tk()
ico_file = os.path.join(os.getcwd(), "iconf.ico")
root.geometry("1920x1080")
root.title('Stat Balance Calculator')
root.iconbitmap(ico_file)
#------------------------------- Images
bg_eqF = PhotoImage(file="Equipement_Slots.png")
#------------------------------- Variaveis de Texto Type de Cada Slot (Setup)
text_helmet = StringVar()
text_cape = StringVar()
text_amulet= StringVar()
text_quiver = StringVar()
text_platebody = StringVar()
text_platelegs = StringVar()
text_weapon = StringVar()
text_shield = StringVar()
text_gloves = StringVar()
text_boots = StringVar()
text_ring = StringVar()
#------------------------------- Variaveis de Background da Label
color_helmet = StringVar()
color_cape = StringVar()
color_amulet = StringVar()
color_quiver = StringVar()
color_platebody = StringVar()
color_platelegs = StringVar()
color_weapon = StringVar()
color_shield = StringVar()
color_gloves = StringVar()
color_boots = StringVar()
color_ring = StringVar()
#------------------------------ Variaveis de Texto Type + Weight
num_helmet = StringVar()
num_cape = StringVar()
num_amulet= StringVar()
num_quiver = StringVar()
num_platebody = StringVar()
num_platelegs = StringVar()
num_weapon = StringVar()
num_shield = StringVar()
num_gloves = StringVar()
num_boots = StringVar()
num_ring = StringVar()
#------------------------------ Variaveis de Texto Type + Weight
total_normal = StringVar()
total_metal = StringVar()
total_ghost = StringVar()
total_wood = StringVar()
total_ice = StringVar()
total_ground = StringVar()
total_fire = StringVar()
total_flying = StringVar()
total_water = StringVar()
total_dragon = StringVar()
total_demon = StringVar()
total_grass = StringVar()
total_poison = StringVar()
total_fighting = StringVar()
total_bug= StringVar()
total_dark = StringVar()
total_rock = StringVar()
total_charge = StringVar()
#---------------------------- Variaveis de Tipo (Top1 e Top2)
top1_type = StringVar()
top2_type = StringVar()
#------------------------------ Funcoes de Inicializacao (Start-up)
Boot_Loader()
Main_2()



