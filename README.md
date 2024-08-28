# acr-assigned

Extensão que verifica se o merge request possui um assigned

```json
{
    "message": "Assignned não atribuído",
    "allowMessage": "Assigned deve ser para algum dos seguintes usuarios: ${USERS}",
    "allowList": [
        "",
        "${AUTHOR_MERGE}"    
    ],
    "denyMessage": "Assigned não pode ser para os seguintes usuarios: ${USERS}",
    "denyList": [
        "",
        "${AUTHOR_MERGE}"
    ]
}
```
