
MONGO QUERIES

To get single pt_page from atsApplyStatus for unique refNum

db.atsApplyStatus.aggregate([
{$match:{lastUpdated: {
$gte: new Date("2023-02-13T00:00:00+05:30"),
$lt: new Date("2023-02-15T00:00:00+05:30")
},"applyType" : {$ne:"JTC"},"applyPlatform":"applyStudio"
}},
{ $group: { _id: "$refNum" ,doc: { $first: "$$ROOT" } } },
{ $project: {refNum: "$doc.refNum", pt_page:"$doc.eventData.current_url",pt_page_1:"$doc.eventData.pt_page",pt_page_3:"$doc.common.referer",platform:"$doc.applyPlatform"} }
])
To get jobSeqNo for all the job with jsqQuestions having all Of
applyFlowConfig_wd -> questionnaireCollection-> workdayQuestionnaireSchema_copy,workdayQuestionnaireSchema
workdayQuestionnaireSchema/ workdayQuestionnaireSchema_copy collection:
db.getCollection("workdayQuestionnaireSchema").aggregate([{$match:{"refNum" : "WORKUS"}},{$project:{"data":{"$objectToArray":"$schema.properties.jsqData.properties"},"_id":0,"questionnaireId":1}},{"$match":{"data.v.allOf":{$exists:1}}},{$project:{"questionnaireId":1}}])
jobInformation collection:
db.jobsInformation.find({refNum:"WORKUS","primaryQuestionnaireId":{$in:["QUESTIONNAIRE-6-67","QUESTIONNAIRE-6-26","QUESTIONNAIRE-6-28","QUESTIONNAIRE-6-64"]}})
.projection({_id:0,jobSeqNo:1})
.sort({_id:-1})
.limit(100)

To get all refNum and jsTemplate_external with specific renderer
db.atsSpecific.find({
jsTemplate_external: mb.regex.contains("/apply/APPLY_form_renderer.js")
}).project({refNum:1,jsTemplate_external:1})
To get jobSeqNo for all the jobs submitted with specific questionnaireId
db.atsApplyStatus.find({refNum:"MARSGLOBAL","jobData.primaryQuestionnaireId":{$in:["QUESTIONNAIRE-6-212"]}})
.projection({jobSeqNo:1})
.sort({_id:-1})
.limit(10)
To get lastUpdated,refNum and username with lastStep true but jsqData empty
db.atsApplyStatus.find({
"lastUpdated": {
$gte: ISODate("2023-02-10T00:00:00.000+0000"),
$lte: ISODate("2023-02-11T00:00:00.000+0000")
},
"isLastStep":true,
"jobData.hasPrimaryQuestionnaire":"yes",
"jsqData":{},
"refNum":"UBNAGLOBAL"
})
.projection({lastUpdated:1,refNum:1,username:1})
.sort({_id:-1})
.limit(100)

SQL QUERIES


To get all unique refNum in version table having contenttype bundles and formtype not jtc and target_env = “production”
SELECT DISTINCT t2.refnum
FROM public."versionMappings" t1
JOIN public."versions" t2 ON t1."versionId" = t2."id"
WHERE t2.formtype <> 'jtc' and t2.contenttype = 'bundles' and t1.target_env = 'Production';


