export class User {
  constructor(
    public username: string,
    public password: string,
  ) {}
}

export class NewUser{
  constructor(
    public username: string,
    public password: string,
    public email: string
  ) {}
}
