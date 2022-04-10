import {Router} from 'express';

// const router = Router();

const GET = (path: string) =>
{
    const __inner_get = (target:any, propertyKey: string, descriptor: PropertyDescriptor) => {
        // this.router.get()
    }
}

function POST()
{

}

class Controller {
    private router : Router;

    constructor(default_path?: string)
    {
        this.router = Router();
    }
}

export default Controller