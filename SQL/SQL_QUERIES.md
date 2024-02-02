
# SQL QUERIES

**To get all unique refNum in version table having contenttype bundles and formtype not jtc and target_env is production**

```
SELECT DISTINCT t2.refnum
FROM public."versionMappings" t1
JOIN public."versions" t2 ON t1."versionId" = t2."id"
WHERE t2.formtype <> 'jtc' and t2.contenttype = 'bundles' and t1.target_env = 'Production';

```
