az resource invoke-action \
  --resource-group rg1 \
  --resource-type  Microsoft.VirtualMachineImages/imageTemplates \
  -n myCustomImage.json \
  --action Run