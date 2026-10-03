import 'package:flutter_test/flutter_test.dart';

import 'package:ezcpos_mobile/core/app.dart';

void main() {
  testWidgets('EZC app starts', (tester) async {
    await tester.pumpWidget(const EzcPosApp());

    expect(find.text('EZC POS'), findsOneWidget);
  });
}
