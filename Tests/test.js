strAsignees = '["a","B"]'

const lstAsignees = JSON.parse(strAsignees)
strAsigneesInfos = ""

for (let i = 0; i < lstAsignees; i++){
    asignee = lstAsignees[i]
    console.log(asignee)
    strAsigneesInfos += `${asignee}\n`
}
console.log(strAsigneesInfos)
return strAsigneesInfos