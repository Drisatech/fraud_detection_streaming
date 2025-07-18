param location string = resourceGroup().location
param containerRegistryName string
param containerName string = 'fraud-api-app'
param imageName string = 'fraud-api:latest'

resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: containerRegistryName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

resource containerGroup 'Microsoft.ContainerInstance/containerGroups@2023-05-01' = {
  name: containerName
  location: location
  properties: {
    containers: [
      {
        name: containerName
        properties: {
          image: '${acr.properties.loginServer}/${imageName}'
          ports: [
            {
              port: 8000
            }
          ]
          resources: {
            requests: {
              cpu: 1.0
              memoryInGb: 1.5
            }
          }
        }
      }
    ]
    osType: 'Linux'
    ipAddress: {
      type: 'Public'
      ports: [
        {
          protocol: 'Tcp'
          port: 8000
        }
      ]
    }
    imageRegistryCredentials: [
      {
        server: acr.properties.loginServer
        username: acr.listCredentials().username
        password: acr.listCredentials().passwords[0].value
      }
    ]
  }
}
