# Accelerator Log

## Options
```json
{
  "functionName" : "main",
  "includeTap" : true,
  "interfaceType" : "http",
  "projectName" : "python-function"
}
```
## Log
```
┏ engine (Chain)
┃  Info Running Chain(GeneratorValidationTransform, UniquePath)
┃ ┏ ┏ engine.transformations[0].validated (Combo)
┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ engine.transformations[0].validated.delegate (Chain)
┃ ┃ ┃  Info Running Chain(Merge, UniquePath)
┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0] (Merge)
┃ ┃ ┃ ┃  Info Running Merge(Combo, Combo, Combo, Combo, Combo, Combo, Combo, Provenance)
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[0] (Combo)
┃ ┃ ┃ ┃ ┃  Info Combo running as Include
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[0].delegate (Include)
┃ ┃ ┃ ┃ ┃  Info Will include [requirements.txt, LICENSE, NOTICE, .gitignore]
┃ ┃ ┃ ┃ ┃ Debug .gitignore matched [requirements.txt, LICENSE, NOTICE, .gitignore] -> included
┃ ┃ ┃ ┃ ┃ Debug .tanzuignore didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug LICENSE matched [requirements.txt, LICENSE, NOTICE, .gitignore] -> included
┃ ┃ ┃ ┃ ┃ Debug README.md didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug cloudevents/func.py didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug func.py didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug functions-icon.png didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┃ Debug manifest.yaml didn't match [requirements.txt, LICENSE, NOTICE, .gitignore] -> excluded
┃ ┃ ┃ ┃ ┗ Debug requirements.txt matched [requirements.txt, LICENSE, NOTICE, .gitignore] -> included
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[1] (Combo)
┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[1].delegate (Chain)
┃ ┃ ┃ ┃ ┃  Info Running Chain(Include, ReplaceText)
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[1].delegate.transformations[0] (Include)
┃ ┃ ┃ ┃ ┃ ┃  Info Will include [func.yaml]
┃ ┃ ┃ ┃ ┃ ┃ Debug .gitignore didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug .tanzuignore didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug LICENSE didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug README.md didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug cloudevents/func.py didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug func.py didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug functions-icon.png didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug manifest.yaml didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┗ Debug requirements.txt didn't match [func.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[1].delegate.transformations[1] (ReplaceText)
┃ ┃ ┃ ┃ ┗ ┗  Info Will replace [main->main]
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[2] (Combo)
┃ ┃ ┃ ┃ ┃  Info Condition (#interfaceType == 'http') evaluated to true
┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[2].delegate (Chain)
┃ ┃ ┃ ┃ ┃  Info Running Chain(Include, ReplaceText)
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[2].delegate.transformations[0] (Include)
┃ ┃ ┃ ┃ ┃ ┃  Info Will include [func.py]
┃ ┃ ┃ ┃ ┃ ┃ Debug .gitignore didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug .tanzuignore didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug LICENSE didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug README.md didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug cloudevents/func.py didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug func.py matched [func.py] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug functions-icon.png didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug manifest.yaml didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┗ Debug requirements.txt didn't match [func.py] -> excluded
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[2].delegate.transformations[1] (ReplaceText)
┃ ┃ ┃ ┃ ┗ ┗  Info Will replace [main->main]
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[3] (Combo)
┃ ┃ ┃ ┃ ┃  Info Condition (#interfaceType == 'cloudevents') evaluated to false
┃ ┃ ┃ ┃ ┗ null ()
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[4] (Combo)
┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[4].delegate (Chain)
┃ ┃ ┃ ┃ ┃  Info Running Chain(Include, ReplaceText)
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[4].delegate.transformations[0] (Include)
┃ ┃ ┃ ┃ ┃ ┃  Info Will include [README.md, DEPLOYING.md]
┃ ┃ ┃ ┃ ┃ ┃ Debug .gitignore didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug .tanzuignore didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md matched [README.md, DEPLOYING.md] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug LICENSE didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug README.md matched [README.md, DEPLOYING.md] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug cloudevents/func.py didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug func.py didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug functions-icon.png didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug manifest.yaml didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┗ Debug requirements.txt didn't match [README.md, DEPLOYING.md] -> excluded
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[4].delegate.transformations[1] (ReplaceText)
┃ ┃ ┃ ┃ ┗ ┗  Info Will replace [python-function->python-function, main->main]
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5] (Combo)
┃ ┃ ┃ ┃ ┃  Info Condition (#includeTap) evaluated to true
┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate (Chain)
┃ ┃ ┃ ┃ ┃  Info Running Chain(Include, ReplaceText, RewritePath, Combo)
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[0] (Include)
┃ ┃ ┃ ┃ ┃ ┃  Info Will include [config/workload.yaml]
┃ ┃ ┃ ┃ ┃ ┃ Debug .gitignore didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug .tanzuignore didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug LICENSE didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug README.md didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug cloudevents/func.py didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml matched [config/workload.yaml] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug func.py didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug functions-icon.png didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug manifest.yaml didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┗ Debug requirements.txt didn't match [config/workload.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[1] (ReplaceText)
┃ ┃ ┃ ┃ ┃ ┗  Info Will replace [python-function->python-function, main->main]
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[2] (RewritePath)
┃ ┃ ┃ ┃ ┃ ┗ Debug Path 'config/workload.yaml' matched '^(?<folder>.*/)?(?<filename>([^/]+?|)(?=(?<ext>\.[^/.]*)?)$)' with groups {ext=.yaml, folder=config/, filename=workload.yaml, g0=config/workload.yaml, g1=config/, g2=workload.yaml, g3=workload.yaml, g4=.yaml} and was rewritten to 'config/workload.yaml'
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3] (Combo)
┃ ┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate (Chain)
┃ ┃ ┃ ┃ ┃ ┃  Info Running Chain(Merge, UniquePath)
┃ ┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate.transformations[0] (Merge)
┃ ┃ ┃ ┃ ┃ ┃ ┃  Info Running Merge(InvokeFragment, Combo)
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate.transformations[0].sources[0] (InvokeFragment)
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate.transformations[0].sources[0].validated (Combo)
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃  Info Condition (#bsGitRepository != null) evaluated to false
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ ┗ null ()
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate.transformations[0].sources[1] (Combo)
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃  Info Combo running as Include
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate.transformations[0].sources[1].delegate (Include)
┃ ┃ ┃ ┃ ┃ ┃ ┃ ┃  Info Will include [**]
┃ ┃ ┃ ┃ ┃ ┃ ┗ ┗ Debug config/workload.yaml matched [**] -> included
┃ ┃ ┃ ┃ ┗ ┗ ╺ engine.transformations[0].validated.delegate.transformations[0].sources[5].delegate.transformations[3].delegate.transformations[1] (UniquePath)
┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[6] (Combo)
┃ ┃ ┃ ┃ ┃  Info Condition (#includeTap) evaluated to true
┃ ┃ ┃ ┃ ┃  Info Combo running as Chain
┃ ┃ ┃ ┃ ┃ engine.transformations[0].validated.delegate.transformations[0].sources[6].delegate (Chain)
┃ ┃ ┃ ┃ ┃  Info Running Chain(Include, ReplaceText)
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[6].delegate.transformations[0] (Include)
┃ ┃ ┃ ┃ ┃ ┃  Info Will include [catalog/catalog-info.yaml]
┃ ┃ ┃ ┃ ┃ ┃ Debug .gitignore didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug .tanzuignore didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug DEPLOYING.md didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug LICENSE didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug README.md didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug catalog/catalog-info.yaml matched [catalog/catalog-info.yaml] -> included
┃ ┃ ┃ ┃ ┃ ┃ Debug cloudevents/func.py didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug config/workload.yaml didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug func.py didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug functions-icon.png didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┃ Debug manifest.yaml didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┗ Debug requirements.txt didn't match [catalog/catalog-info.yaml] -> excluded
┃ ┃ ┃ ┃ ┃ ┏ engine.transformations[0].validated.delegate.transformations[0].sources[6].delegate.transformations[1] (ReplaceText)
┃ ┃ ┃ ┃ ┗ ┗  Info Will replace [python-function->python-function]
┃ ┃ ┃ ┗ ╺ engine.transformations[0].validated.delegate.transformations[0].sources[7] (Provenance)
┃ ┗ ┗ ╺ engine.transformations[0].validated.delegate.transformations[1] (UniquePath)
┗ ╺ engine.transformations[1] (UniquePath)
```
