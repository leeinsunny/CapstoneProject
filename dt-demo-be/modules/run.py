import argparse
import os

# Use following importing commands 
# when running API
import modules.slang.run as slang
import modules.pdd.run as pdd
import modules.dup.run as dup
import modules.typo.run as typo
import modules.spc.run as spc

# Use following importing commands 
# when running /modules/run.py directly(not from API)
# import slang.run as slang
# import pdd.run as pdd
# import dup.run as dup
# import typo.run as typo
# import spc.run as spc

def runModule(args):
    # TODO: update module list info
    # Typo must run prior to other modules
    module_list = {
       "typo": {
          "enabled": False,
          "module": typo
       },
       "slang": {
          "enabled": False,
          "module": slang
       },
       "pdd": {
          "enabled": False,
          "module": pdd
       },
       "dup": {
          "enabled": False,
          "module": dup
       },
    }

    if args.modules:
    # When specific modules have been selected
        delimiter = ','
        mlist = args.modules.split(delimiter)
        print("modules value:", mlist)
        # Enable given module
        for modules_info in module_list:
            if modules_info in mlist:
                print(f"{modules_info} module enabled.")
                module_list[modules_info]["enabled"] = True
    elif args.all:
    # When `all` option enabled
        print("all option:", args.all)
        # Enable every module option
        for modules_info in module_list:
            module_list[modules_info]["enabled"] = True
    else:
    # Default option (not defined)
    # TODO: define default option
        print("module value not given.")
        print("Default value option is to enable all modules")
        for modules_info in module_list:
            module_list[modules_info]["enabled"] = True
    
    print("input value:", args.input)
    fileName = args.input
    
    filterTimes = 0
    for modules_info in module_list:
       if module_list[modules_info]["enabled"]:
           print(f">>>>>>> {modules_info} module is enabled.")
           module_list[modules_info]["module"].run(fileName)
           fileName = fileName.replace(".txt", "_filtered.txt")
           filterTimes += 1
   
   # Remove unnecessary files.
   # TODO: would it be better to save whole files?
    db_dir = os.path.join("..", "database")
    original_name = args.input.replace(".txt","")
    for i in range(1,filterTimes,+1):
        fileNotUsed_name = original_name+"_filtered"*i+".txt"
        fileNotUsed_dir = os.path.join(db_dir, fileNotUsed_name)
        os.remove(fileNotUsed_dir)
    if(filterTimes > 1):
        last_name = original_name+"_filtered"*filterTimes+".txt"
        last_dir = os.path.join(db_dir, last_name)
        final_dir = os.path.join(db_dir, original_name+"_filtered"+".txt")
        os.rename(last_dir, final_dir)

def main() :
  argparser = argparse.ArgumentParser(
    description = "<Run cleansing modules>"
  )

  argparser.add_argument(
     '-a',
     '--all',
     action='store_true',
     help="Run all modules"
  )

  argparser.add_argument(
     '-m',
     '--modules',
     type=str,
     help='Put module types in list, i.e)"slang,pdd"'
  )

  argparser.add_argument(
    '--input',
    metavar='I',
    type=str,
    default='fake.txt',
    help='Put input sentence or word in String type'
  )

  args = argparser.parse_args()
  return runModule(args)

if __name__ == "__main__":
  main()