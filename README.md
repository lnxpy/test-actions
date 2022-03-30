### Testing GitHub Actions with CodeHub APIs
> :fire: Testing Github Actions as a CI tool for testing pull requests on [@codehub-ir](github.com/codehub-ir) APIs.

> :page_facing_up: [Check the blog post for more information about the implementation and concepts](https://imsadra.me/lights-camera-github-actions).

### Opearations
***NOT TOO SHABBY!*** Aim is to have a Continous Integration (CI) system on [Codehub's Snippet Push API](https://codehub.pythonanywhere.com/api/v1/docs#operation/snippet_create). There is a simple Pythonic class tries to interact with the endpoint and send the provided data to the endpoint. There is only one test case testing the post request with the provided data.
