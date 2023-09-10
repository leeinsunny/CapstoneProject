import modules.slang.run as slang
import modules.pdd.run as pdd
import modules.dup.run as dup
import modules.typo.run as typo
import argparse

def runModule(args):
    # TODO: update module list info
    module_list = {
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
       "typo": {
          "enabled": False,
          "module": typo
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
    # slang.run("demo.txt")
    for modules_info in module_list:
       if module_list[modules_info]["enabled"]:
           print(f"{modules_info} module is enabled.")
           module_list[modules_info]["module"].run(args.input)

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