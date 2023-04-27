# Blue/green deployments on ECS Fargate with Codepipeline - Examples

**Note**: this is example source code and should not be used in production. It should be used as a reference only.

An example about deploying a Nginx web server on ECS Fargate with blue/green strategy.

More info here:
- [Blue/green deployment of a web server on ECS Fargate](https://letsmake.cloud/bluegreen-fargate)

To get started:
- Deploy terraform using `terraform apply`
- Connect AWS CodeCommit repo to `sourcecode` directory
- Push up code from `sourcecode` directory to `main` branch
- This will kick-off the B/G AWS Code Deploy process
- `terraform apply` changes can still be made directly

- Don't forget to change the AWS Account ID in the `sourcecode/taskdef.json` file otherwise the deployment will fail
- This can be automated as well but is not in this example