# Mine Alliance - Reinventing a sustainable future for Arizona Mining Industry with AI 🚀

An innovative, AI-driven application designed to unite stakeholders across Arizona's mining industry, promoting responsible and sustainable practices.

<!-- Live Demo: [Mine Alliance](http://54.245.158.146:3000/) -->
- Demo: [Youtube](https://www.youtube.com/watch?v=7ei89DcPWfY)
- Wireframe: [Figma](https://www.figma.com/proto/8R9e3nz8XQjVrb684ZGR8j/AZ-AI-Sustainability-Hack?node-id=0-1&t=5BL2uzE0XvacWGkw-1)
- DevPost: [DEVPOST](https://devpost.com/software/mine-alliance#updates)
- Vercel: [Static Deployment](https://sustainable-az-spark-challenge-g3sayr8rs-luaannguyens-projects.vercel.app/)

![Mine Alliance](MineAlliance.png)

## Inspiration ✨

Once we learned that the majority of mining sites were on Indigenous land, some of it sacred land, and that the local communities had no power to raise objections or even to aquire information on the mines affecting their area. We felt motivated to give local communities the power of free information and a voice that was on equal footing with major mining companies and state and federal regulators, so that they could be a part in the process of mining minerals that are essential to human society.

## What it does ⛏️

Our website allows the three major stakeholders to log-in either as a community member, mining site representative, or government regulator. Where then, the individual can see information on nearby active mines including tenure; effect radius of the mine; water, soil, and air quality; biodiversity impact; socioeconomic impact; and a description of the mine. Depending on who's logged-in different options will be available. Community members can submit issues that they find with specific mining sites, whether it is an ecological issue or a disruption to sacred lands. Government regulators can submit new site specific regulations, giving a title to the new regulation and a description of the regulation. Mining site representatives can respond to feedback given on their mining sites and submit announcements that can be seen by everyone.

## How we build it 👷

![Archtecture](architecture.png)

### Front-end

- `NextJS` for SEO optimization and server-side rendering
- `TailwindCSS` for utility-first styling
- `Shadcn` for modern UI components and design system
- `Framermotion` for smooth, modern website animations
- `Leaflet` for interactive map and geospatial visualizations
- `Vercel` for seamless deployment and front-end hosting
- `Lucide` for modern icons

### Back-end & DevOps

- `Flask` for handling HTTP requests and API development
- `SQLAlchemy` for robust database management and ORM
- `AWS EC2` for scalable and flexible cloud computing infrastructure
- `Amazon SageMaker Studio` for builidng, training, and deploying geologically intelligent model
- `ChatGPT-4` API intergration for advanced NLP

## Challenges we ran into 🚒

- Collecting enough data: Some mining data were confidential to the public.
- Communication Issue between members: this is our first hackathon together.
- AWS Credit Time limit: We weren't able to fully fine-tune our own AI model due to a limited AWS credit.
- Cross-origin hosting: While hosting both client and server on AWS EC2, we ran into the deployment problem due to hosts unable to recognize/ fetch data on the same origin. It turned out to be NextJS environment variables' imcompatibility with AWS hosting.

## Accomplishments that we're proud of 👍

We spent a lot of time researching what specific information to show that would be relevant for our stakeholders and what goes into creating an impact assessment.

## How to run the program 💻

Make sure you have latest `NodeJS`, `Pip`, `npm`, and `Python` installed.

### Client - `Running on http://127.0.0.1:3000`

```shell
> cd client
> npm i #install all dependencies if this is the first time you are doing this
> npm ci (optional)
> npm run build (for production)
> npm run dev
```

### Server - `Running on http://127.0.0.1:5000`

```shell
> cd server
> python3 -m venv venv
> source venv/bin/activate
> pip install  -r requirements.txt
> python3 db_init.py (If you don't have the data already)
> python3 app.py
```

### Envrionments variables 🤐

Create a .env files in both `client` and `server`

In Client, you need Stadia Map's API key and backend url depending on your production needs:

- `STADIA_MAPS_API_KEY=YOUR_KEY`
- `BACKEND_URL=YOUR_HOST`

In Server, you need OpenAI's API:

- `OPENAI_API_KEY=`YOUR_KEY

# 🪪 License

`Mine Alliance` is licensed under MIT License. All development is currently maintain by [Luan Nguyen](https://github.com/LuaanNguyen).
