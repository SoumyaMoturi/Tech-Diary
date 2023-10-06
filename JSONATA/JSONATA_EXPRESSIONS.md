
 # JSONATA EXPRESSIONS


**To remove special characters from jobResponsibilities in experienceData**

```

{ "experienceData": [$map($.experienceData, function($experience, $i, $a) {
$merge($append($spread($.experienceData[$i]),{"description": $replace($experience.description,/[/\\`?'"&]/,'')
}))
})]}

```

**To send another key in formData (“otherEmployer”) if we add a new value other than options we have in typeAhead when option values or in numeric way and entered value contains alphabets.**

```

{
     "experienceData": [$map($.experienceData, function($experience, $i, $a) {
        $merge($append($spread($experience), 
                $experience.companyName.$contains(/[a-zA-Z]/)?{ "otherCompanyName" : $experience.companyName,"companyName": "99998"}                  
   ))
})]}

```

**To send displayName for dropdowns along with value in formData**

```

(
$country := schema.schema.properties.country;
{
"countryName": $country.enum ~> $map(function($v, $i) { $v = formData.country ? $country.enumNames[$i] })
}
)

```

**To populate data in applygetReferences to enum and enumNames**

```

{
"enum": NODE_DATA.w6Xdsuhsj.applyGetReferences.data.values.key? [NODE_DATA.w6Xdsuhsj.applyGetReferences.data.values.key]:[],
"enumNames": NODE_DATA.w6Xdsuhsj.applyGetReferences.data.values.label? [NODE_DATA.w6Xdsuhsj.applyGetReferences.data.values.label]:[]
}

```


**To delete a specific key from Object**

```

	$ ~> |$.properties|{}, ['applyJSType', 'apiCredentialHeading']|
To fetched keys from object and removing a specific word from key
$each(NODE_DATA.idFHzWO77lg, function($v, $k) {$count($v)>0 ? $replace($k, [STRING_TO_BE_REPLACED], "") })

```

**To sum up a specific field (named f1) which satisfies the condition from all objects (named obj) in an array**

```

obj[f1 > value].f1 ~> $sum

```

**To get the count of fields based on a substring value**

```

obj[$substring(f1,0,3)=”yes”] ~> $count

```

**Recursive Function to fetch all keys in schema i.e. (firstname,experienceData.employer,experienceData.Date.startDate)**

```

(
$fetch := function($o, $prefix) {
$each($o, function($v, $k) {(
$name := $join([$prefix,$k], '.');
($v.type) = 'object' ? $fetch($v.properties, $name): ($v.type) = 'array'?$fetch($v.items.properties, $name) : {$name:""}
)}) ~> $merge()
};
$filterForm := function($obj, $formtype) {$filter($obj,function($v){$v.type = $formtype})};
{
"enum": $keys($fetch(NODE_DATA.idEDAf82KXa.published_form)),
"enumNames": $keys($fetch(NODE_DATA.idEDAf82KXa.published_form))
}
)

```



**Expression to add a new key to a specific object based on index in an array of Objects.**
 
 ```
 (
     $ind := $split($split(changed_field, '[')[1], ']')[0];
     {
    "category_mapping": $map(category_mapping,function($item, $index) {
                $index  =  $number($ind) ? ($new := $append([$item],[{"newval":"newval"}]);
                                $merge($new)): $item
 	})
}
  )

```

**Expression to get only specific values from each object in array of Objects**

```

   array.{ field1: property1, field2: property2, field3: property3 }

```

**To remove if endDate is empty**

```

 { "experienceData": [$map($.experienceData, function($experience, $i, $a) {
     $experience.fromTo.endDate = "" ?  ($experience ~> |fromTo|{}, ['endDate']|) : $experience
})]}

```











 
