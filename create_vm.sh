#!/bin/bash
echo 'Creando Grupo de Recursos para la vm'
az group create \
    --name rg \
    --location eastus

echo 'Creando la Virtual Machine'
az vm create \
    --resource-group rg \
    --name vm1 \
    --image UbuntuLTS \
    --admin-username carlos \
    --ssh-key-values mykeys.pub \
    --size Standard_D2s_v3 \
