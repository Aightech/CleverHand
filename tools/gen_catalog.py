import os
import yaml
import csv
import json

#open specs yaml
sku_format = {}
with open("docs/specs/sku_schema.yaml", "r") as f:
    sku_format = yaml.safe_load(f)
sku_prefix = sku_format["sku"]["prefix"]
sku_sep = sku_format["sku"]["separator"]
sku_catmap = sku_format["fields"]["CATEGORY"]["allowed"]
sku_catmapRev = {v[0]: [k, v[1]] for k, v in sku_catmap.items()}
sku_fammap = sku_format["fields"]["FAMILY"]["allowed"]
sku_fammapRev = {v[0]: [k, v[1]] for k, v in sku_fammap.items()}

destinaion_path = "catalog/"


def get_module_description(root):
    """Extract the description from the yaml file"""
    with open(os.path.join(root, "description.yaml"), "r") as f:
        desc = yaml.safe_load(f)
    
    return desc


def check_SKU(sku, path):
    """Check the SKU format."""
    # check each field are in map
    skul = sku.split(sku_sep)
    if len(skul) != 4:
        print(f"SKU {sku} has wrong format")
        return False
    if skul[0] != sku_prefix:
        print(f"SKU {sku} has wrong prefix")
        return False
    if skul[1] not in sku_catmap:
        print(f"SKU {sku} has wrong category {skul[1]} not in {sku_catmap}")
        return False
    if skul[2] not in sku_fammap:
        print(f"SKU {sku} has wrong family {skul[2]} not in {sku_fammap}")
        return False
    if skul[3] != path.split("/")[-1].upper():
        print(f"SKU {sku} has wrong model {skul[3]} not in {path.split('/')[-1].upper()}")
        return False
    return True


def get_modules(modules_path):
    """Get the list of modules."""
    modules = {}
    for root in modules_path:
        desc = get_module_description(root)
        # check sku
        if not check_SKU(desc["sku"], desc["location"]+"/"+desc["id"]):
            raise ValueError(f"SKU {desc['sku']} does not match classification {desc['classification']}")
        cll = ["CH", desc["classification"]["category"], desc["classification"]["family"], desc["classification"]["model"]]
        #  print ok in green
        print("\033[92mOK\033[0m "+ f" {cll[3]:20} {cll[2]:20} {cll[3]}")
        # add to modules
        if cll[1] not in modules:
            modules[cll[1]] = {}
        if cll[2] not in modules[cll[1]]:
            modules[cll[1]][cll[2]] = {}
        modules[cll[1]][cll[2]][cll[3]] = {"status": desc["readiness"], "sku": desc["sku"], "path": desc["location"], "description": desc["description"]}     
    return modules
        
def scan_hardware_folder():
    """Scan the hardware folder for module entries."""
    paths = []
    for root, dirs, files in os.walk("hardware/CleverHand-hardware/pcb/"):
        if "description.yaml" in files:    
            paths.append(root)
    return paths

def make_yaml_catalog(modules):
    """Make a catalog of all the modules."""
    with open(destinaion_path+"/modules.yaml", "w") as f:
        yaml.dump(modules, f,sort_keys=False)

def make_json_catalog(modules):
    """Make a catalog of all the modules."""
    with open(destinaion_path+"/modules.json", "w") as f:
        json.dump(modules, f,sort_keys=False)

def make_csv_catalog(modules):
    """Make a catalog of all the modules."""
    with open(destinaion_path+"/modules.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Family", "Model", "Status", "SKU", "Path", "Description"])
        for cat in modules:
            for fam in modules[cat]:
                for model in modules[cat][fam]:
                    writer.writerow([cat, fam, model, modules[cat][fam][model]["status"], modules[cat][fam][model]["sku"], modules[cat][fam][model]["path"], modules[cat][fam][model]["description"]])


def main():
    modules_path = scan_hardware_folder()
    modules = get_modules(modules_path)
    make_yaml_catalog(modules)
    make_csv_catalog(modules)
    make_json_catalog(modules)
    

if __name__ == "__main__":
    main()