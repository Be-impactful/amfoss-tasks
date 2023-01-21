import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(const MyApp());
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.landscapeLeft,
    DeviceOrientation.landscapeRight]);
  SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter App amfoss',
      home:  MyHomePage(title: 'My First App!'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double x_position = 0;
  double y_position = -680;


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          AnimatedPositioned(
              top: y_position,
              right: x_position,
              child: Image.asset("img/background.png"),
              duration: Duration(microseconds: 200)),
          Positioned(
              top: 200,
              left: 400,
              child: Container(
                height: 195,
                width: 195,
                decoration: BoxDecoration(
                    image: DecorationImage(
                      image: AssetImage(
                          "img/bunny.png"
                      ),
                      fit: BoxFit.fill,
                    )
                ),
              )),
          Positioned(
              top: 300,
              left: 120,
              child: IconButton(
                icon: Icon(Icons.keyboard_arrow_right_rounded),

                onPressed: () {
                  setState(() {
                    if (x_position < 0) {
                      x_position += 10;
                    }
                  });
                },
              )),
          Positioned(
              top: 300,
              left: 10,
              child: IconButton(
                icon: Icon(Icons.keyboard_arrow_left_rounded),
                onPressed: () {
                  setState(() {
                    if (x_position >= -1100) {
                      x_position -= 10;
                    }
                  });
                },
              )),
          Positioned(
              top: 250,
              left: 65,
              child: IconButton(
                icon: Icon(Icons.keyboard_arrow_up_rounded),
                onPressed: () {
                  setState(() {
                    if (y_position < 0) {
                      y_position += 10;
                    }
                  });
                },
              )),
          Positioned(
              top: 350,
              left: 65,
              child: IconButton(
                icon: Icon(Icons.keyboard_arrow_down_rounded),
                onPressed: () {
                  setState(() {
                    if (y_position > -680) {
                      y_position -= 10;
                    }
                  });
                },
              )),
        ],
      ),
    );
  }
}